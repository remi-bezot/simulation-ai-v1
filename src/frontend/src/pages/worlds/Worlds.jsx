import React, { useEffect, useState } from "react";
import WorldList from "../../components/worlds/WorldList";
import { Box, Typography } from "@mui/material";
import { get } from "../../services/api";

const Worlds = () => {
  const [worlds, setWorlds] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await get("/api/worlds");
        setWorlds(response.worlds);
      } catch (err) {
        setError("Erreur lors de la récupération des mondes.");
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  if (loading) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center" height="100vh">
        <Typography>Chargement des mondes...</Typography>
      </Box>
    );
  }

  if (error) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center" height="100vh">
        <Typography color="error">{error}</Typography>
      </Box>
    );
  }

  return (
    <Box padding={3}>
      <Typography variant="h4" gutterBottom>
        Liste des Mondes
      </Typography>
      <WorldList worlds={worlds} />
    </Box>
  );
};

export default Worlds;
