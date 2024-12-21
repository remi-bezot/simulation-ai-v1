import React, { useState, useEffect, useMemo } from "react";
import {
  Typography,
  Card,
  CardContent,
  CardActions,
  Button,
  Grid,
  CardHeader,
  Avatar,
  IconButton,
  Collapse,
  Skeleton,
  Pagination,
  TextField,
  MenuItem,
  Snackbar,
  Alert,
  CircularProgress,
} from "@mui/material";
import { deepPurple, orange } from "@mui/material/colors";
import DeleteIcon from "@mui/icons-material/Delete";
import EditIcon from "@mui/icons-material/Edit";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import chroma from "chroma-js";
import { useTheme } from "@mui/material/styles";

const isValidHexColor = (color) => chroma.valid(color);

// Composant SkeletonCard pour le chargement
const SkeletonCard = React.memo(() => (
  <Grid item xs={12} sm={6} md={4}>
    <Card elevation={5}>
      <CardHeader
        avatar={<Skeleton variant="circular" width={40} height={40} />}
        title={<Skeleton width="60%" />}
        subheader={<Skeleton width="40%" />}
      />
      <CardContent>
        <Skeleton variant="rectangular" height={60} />
      </CardContent>
      <CardActions>
        <Skeleton width="30%" />
        <Skeleton width="20%" />
      </CardActions>
    </Card>
  </Grid>
));

// Composant DimensionCard (pour chaque carte)
const DimensionCard = React.memo(
  ({
    dimension,
    selected,
    onSelect,
    onEdit,
    onDelete,
    onExpand,
    expanded,
    index,
    theme,
  }) => {
    return (
      <Grid
        item
        xs={12}
        sm={6}
        md={4}
        key={index}
        style={{
          transition: "transform 0.2s ease-in-out",
          transform: "scale(1)",
        }}
        onMouseEnter={(e) => {
          e.currentTarget.style.transform = "scale(1.05)";
        }}
        onMouseLeave={(e) => {
          e.currentTarget.style.transform = "scale(1)";
        }}
      >
        <Card
          elevation={5}
          style={{
            backgroundColor: isValidHexColor(dimension.color)
              ? dimension.color
              : theme.palette.background.paper,
            color: isValidHexColor(dimension.color)
              ? chroma.contrast(dimension.color, "white") > 4.5
                ? "#fff"
                : "#000"
              : theme.palette.text.primary,
            border: selected ? `2px solid ${orange[500]}` : "none",
          }}
        >
          <CardHeader
            avatar={
              <Avatar
                sx={{
                  bgcolor: deepPurple[500],
                }}
                aria-label={`Avatar de la dimension ${dimension.name}`}
              >
                {dimension.name ? dimension.name[0].toUpperCase() : "D"}
              </Avatar>
            }
            title={dimension.name}
            subheader={dimension.description || "Pas de description"}
            action={
              <>
                <IconButton
                  aria-label="modifier la dimension"
                  onClick={() => onEdit(dimension)}
                >
                  <EditIcon />
                </IconButton>
                <IconButton
                  aria-label="supprimer la dimension"
                  onClick={() => onDelete(dimension.id)}
                >
                  <DeleteIcon />
                </IconButton>
              </>
            }
          />
          <CardContent>
            <Typography variant="body2">
              {dimension.details || "Aucun détail supplémentaire disponible."}
            </Typography>
          </CardContent>
          <CardActions>
            <Button
              size="small"
              variant="outlined"
              onClick={() => onSelect(dimension)}
            >
              Explorer
            </Button>
            <IconButton
              onClick={() => onExpand(index)}
              aria-expanded={expanded}
              aria-label="Afficher plus"
            >
              <ExpandMoreIcon />
            </IconButton>
          </CardActions>
          <Collapse in={expanded} timeout="auto" unmountOnExit>
            <CardContent>
              <Typography paragraph>
                {dimension.details || "Pas d'informations supplémentaires."}
              </Typography>
            </CardContent>
          </Collapse>
        </Card>
      </Grid>
    );
  }
);

// Barre de recherche et tri
const FilterBar = React.memo(({ searchTerm, onSearchChange, sortBy, onSortChange }) => (
  <Grid container spacing={2} style={{ marginBottom: "20px" }}>
    <Grid item xs={12} sm={6}>
      <TextField
        label="Rechercher une dimension"
        variant="outlined"
        fullWidth
        value={searchTerm}
        onChange={onSearchChange}
      />
    </Grid>
    <Grid item xs={12} sm={6}>
      <TextField
        label="Trier par"
        variant="outlined"
        fullWidth
        select
        value={sortBy}
        onChange={onSortChange}
      >
        <MenuItem value="name">Nom</MenuItem>
        <MenuItem value="created_at">Date de création</MenuItem>
      </TextField>
    </Grid>
  </Grid>
));

// Composant principal MultiverseList
const MultiverseList = ({
  dimensions = [],
  onSelectDimension,
  selectedDimension,
  onEditDimension,
  onDeleteDimension,
  isLoading = false,
  error = null,
  onReload,
}) => {
  const theme = useTheme();
  const [expandedIndex, setExpandedIndex] = useState(null);
  const [currentPage, setCurrentPage] = useState(1);
  const [searchTerm, setSearchTerm] = useState("");
  const [sortBy, setSortBy] = useState("name");
  const itemsPerPage = 6;

  const filteredAndSortedDimensions = useMemo(() => {
    const filtered = dimensions.filter((dimension) =>
      dimension.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    const sorted = [...filtered].sort((a, b) => {
      if (sortBy === "name") {
        return a.name.localeCompare(b.name);
      }
      if (sortBy === "created_at") {
        return new Date(b.created_at) - new Date(a.created_at);
      }
      return 0;
    });
    return sorted;
  }, [dimensions, searchTerm, sortBy]);

  const paginatedDimensions = useMemo(() => {
    const startIndex = (currentPage - 1) * itemsPerPage;
    return filteredAndSortedDimensions.slice(
      startIndex,
      startIndex + itemsPerPage
    );
  }, [filteredAndSortedDimensions, currentPage]);

  const handleExpandClick = (index) => {
    setExpandedIndex(expandedIndex === index ? null : index);
  };

  const handlePageChange = (_, value) => {
    setCurrentPage(value);
  };

  return (
    <div>
      {isLoading ? (
        <Grid container spacing={3}>
          {Array.from(new Array(itemsPerPage)).map((_, index) => (
            <SkeletonCard key={index} />
          ))}
        </Grid>
      ) : error ? (
        <Grid container justifyContent="center" alignItems="center">
          <Alert
            severity="error"
            action={
              <Button color="inherit" size="small" onClick={onReload}>
                Réessayer
              </Button>
            }
          >
            Une erreur est survenue lors du chargement des dimensions.
          </Alert>
        </Grid>
      ) : dimensions.length > 0 ? (
        <>
          <FilterBar
            searchTerm={searchTerm}
            onSearchChange={(e) => setSearchTerm(e.target.value)}
            sortBy={sortBy}
            onSortChange={(e) => setSortBy(e.target.value)}
          />
          <Grid container spacing={3}>
            {paginatedDimensions.map((dimension, index) => (
              <DimensionCard
                key={index}
                dimension={dimension}
                selected={selectedDimension?.name === dimension.name}
                onSelect={onSelectDimension}
                onEdit={onEditDimension}
                onDelete={onDeleteDimension}
                onExpand={handleExpandClick}
                expanded={expandedIndex === index}
                index={index}
                theme={theme}
              />
            ))}
          </Grid>
          <Grid container justifyContent="center" style={{ marginTop: "20px" }}>
            <Pagination
              count={Math.ceil(filteredAndSortedDimensions.length / itemsPerPage)}
              page={currentPage}
              onChange={handlePageChange}
              color="primary"
            />
          </Grid>
        </>
      ) : (
        <Typography
          color="textSecondary"
          style={{ textAlign: "center", marginTop: "20px", fontStyle: "italic" }}
        >
          Aucune dimension disponible. Essayez d'en ajouter une !
        </Typography>
      )}
    </div>
  );
};

export default MultiverseList;
