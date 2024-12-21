import React, { useEffect, useState } from "react";
import Multiverse from "../../components/multiverse/Multiverse";
import MultiverseList from "../../components/multiverse/MultiverseList";
import SimulationControls from "../../components/simulation/SimulationControls";
import { Box, Typography, Button, Alert, CircularProgress } from "@mui/material";
import { get, addDimension, deleteDimension, updateDimension } from "../../services/api";

const MultiversePage = () => {
  const [dimensions, setDimensions] = useState([]);
  const [selectedDimension, setSelectedDimension] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [rotationSpeed, setRotationSpeed] = useState(1); // Vitesse de rotation par défaut
  const [actionInProgress, setActionInProgress] = useState(false); // État d'action en cours

  // Fonction pour récupérer les données
  const fetchDimensions = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await get("/api/multiverse");
      setDimensions(response.multiverse); // Assurez-vous que la clé `response.multiverse` correspond à l'API
    } catch (err) {
      setError("Erreur lors de la récupération des dimensions.");
    } finally {
      setLoading(false);
    }
  };

  // Gestion de la sélection d'une dimension
  const handleSelectDimension = (dimension) => {
    setSelectedDimension(dimension); // Met à jour la dimension sélectionnée
  };

  // Ajout d'une nouvelle dimension (synchronisée avec le backend)
  const handleAddDimension = async (name, color) => {
    if (actionInProgress) return; // Empêche les actions multiples
    setActionInProgress(true);
    const newDimension = {
      name,
      color: parseInt(color.replace("#", ""), 16), // Convertit la couleur hex en décimal
      description: "Nouvelle dimension ajoutée dynamiquement.",
    };
    try {
      const addedDimension = await addDimension(newDimension);
      setDimensions((prevDimensions) => [...prevDimensions, addedDimension]);
    } catch (err) {
      setError("Erreur lors de l'ajout de la dimension.");
    } finally {
      setActionInProgress(false);
    }
  };

  // Suppression d'une dimension (synchronisée avec le backend)
  const handleRemoveDimension = async (dimensionId) => {
    if (actionInProgress || dimensions.length === 0) return; // Empêche les actions multiples ou si vide
    setActionInProgress(true);

    try {
      await deleteDimension(dimensionId); // Supprime côté backend
      setDimensions((prevDimensions) =>
        prevDimensions.filter((dim) => dim.id !== dimensionId)
      );
    } catch (err) {
      setError("Erreur lors de la suppression de la dimension.");
    } finally {
      setActionInProgress(false);
    }
  };

  // Modification d'une dimension (synchronisée avec le backend)
  const handleEditDimension = async (updatedDimension) => {
    if (actionInProgress) return; // Empêche les actions multiples
    setActionInProgress(true);

    try {
      const response = await updateDimension(updatedDimension.id, updatedDimension);
      setDimensions((prevDimensions) =>
        prevDimensions.map((dim) =>
          dim.id === updatedDimension.id ? { ...dim, ...response } : dim
        )
      );
    } catch (err) {
      setError("Erreur lors de la modification de la dimension.");
    } finally {
      setActionInProgress(false);
    }
  };

  // Réinitialiser la sélection si la dimension est supprimée ou introuvable
  useEffect(() => {
    if (selectedDimension && !dimensions.some((dim) => dim.name === selectedDimension.name)) {
      setSelectedDimension(null);
    }
  }, [dimensions, selectedDimension]);

  useEffect(() => {
    fetchDimensions();
  }, []);

  if (loading) {
    return (
      <Box
        display="flex"
        justifyContent="center"
        alignItems="center"
        height="100vh"
      >
        <CircularProgress />
        <Typography style={{ marginLeft: "10px" }}>Chargement des dimensions...</Typography>
      </Box>
    );
  }

  return (
    <Box padding={3}>
      <Typography variant="h4" gutterBottom>
        Dimensions Multivers
      </Typography>

      {/* Affichage des erreurs */}
      {error && (
        <Alert severity="error" style={{ marginBottom: "20px" }}>
          {error}
        </Alert>
      )}

      {/* Contrôles de la simulation */}
      <SimulationControls
        onStart={() => console.log("Simulation démarrée")}
        onStop={() => console.log("Simulation arrêtée")}
        onReset={() => fetchDimensions()} // Recharge les dimensions depuis le backend
        onSpeedChange={(speed) => setRotationSpeed(speed)} // Met à jour la vitesse de rotation
        onAddSphere={handleAddDimension} // Ajoute une nouvelle dimension
        onRemoveSphere={() =>
          handleRemoveDimension(selectedDimension?.id) // Supprime la dimension sélectionnée
        }
      />

      {/* Vue 3D avec dimension mise en évidence */}
      <Multiverse
        dimensions={dimensions}
        highlightedDimension={selectedDimension}
        rotationSpeed={rotationSpeed} // Passe la vitesse de rotation à la 3D
        onDimensionClick={handleSelectDimension} // Synchronisation avec les clics dans la 3D
      />

      {/* Liste textuelle des dimensions */}
      <MultiverseList
        dimensions={dimensions}
        selectedDimension={selectedDimension}
        onSelectDimension={handleSelectDimension}
        onDeleteDimension={handleRemoveDimension} // Supprime depuis la liste
        onEditDimension={handleEditDimension} // Édite depuis la liste
      />
    </Box>
  );
};

export default MultiversePage;
