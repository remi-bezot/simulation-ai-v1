import React, { useEffect, useState } from "react";
import Simulation3D from "../../components/simulation/Simulation3D";
import SimulationStats from "../../components/simulation/SimulationStats";
import SimulationControls from "../../components/simulation/SimulationControls";
import { Box, Typography } from "@mui/material";
import { get } from "../../services/api";

const Simulation = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [speed, setSpeed] = useState(1);
  const [isRunning, setIsRunning] = useState(false);

  // Récupération des données de simulation
  const fetchData = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await get("/api/simulation");
      setData(response.items);
    } catch (err) {
      setError("Erreur lors de la récupération des données de simulation.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  // Configuration de l'objet 3D
  const getObject3D = (item, index) => {
    const geometry = new THREE.SphereGeometry(0.5, 32, 32);
    const material = new THREE.MeshStandardMaterial({
      color: item.color || 0x007bff,
    });
    const sphere = new THREE.Mesh(geometry, material);
    sphere.position.x = index * 2 - (data.length - 1);
    return sphere;
  };

  // Animation des objets
  const animation = (objects) => {
    if (isRunning) {
      objects.forEach((object) => {
        object.rotation.y += 0.01 * speed;
      });
    }
  };

  // Gestion des contrôles
  const handleStart = () => setIsRunning(true);
  const handleStop = () => setIsRunning(false);
  const handleReset = () => {
    setIsRunning(false);
    setSpeed(1);
  };

  if (loading) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center" height="100vh">
        <Typography>Chargement de la simulation...</Typography>
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
        Simulation 3D
      </Typography>
      <Simulation3D data={data} getObject3D={getObject3D} animation={animation} />
      <SimulationStats data={data} />
      <SimulationControls
        onStart={handleStart}
        onStop={handleStop}
        onReset={handleReset}
        onSpeedChange={setSpeed}
      />
    </Box>
  );
};

export default Simulation;
