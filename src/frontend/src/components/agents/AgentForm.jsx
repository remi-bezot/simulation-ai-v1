import React, { useState } from "react";
import { Box, TextField, Button, Typography } from "@mui/material";
import { post } from "../../services/api";

const AgentForm = ({ onAgentAdded }) => {
  const [name, setName] = useState("");
  const [properties, setProperties] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const propertiesObject = properties
        ? JSON.parse(properties)
        : {}; // Convertir les propriétés en objet
      await post("/api/agents", { name, properties: propertiesObject });
      setName("");
      setProperties("");
      onAgentAdded(); // Callback pour rafraîchir la liste des agents
    } catch (err) {
      console.error("Erreur lors de la création de l'agent :", err);
      setError("Impossible de créer l'agent.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box component="form" onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
      <Typography variant="h6" gutterBottom>
        Ajouter un nouvel agent
      </Typography>
      {error && <Typography color="error">{error}</Typography>}
      <TextField
        label="Nom de l'agent"
        value={name}
        onChange={(e) => setName(e.target.value)}
        fullWidth
        required
        style={{ marginBottom: "10px" }}
      />
      <TextField
        label="Propriétés (JSON)"
        value={properties}
        onChange={(e) => setProperties(e.target.value)}
        fullWidth
        multiline
        rows={3}
        placeholder='{"role": "explorateur"}'
        style={{ marginBottom: "10px" }}
      />
      <Button
        type="submit"
        variant="contained"
        color="primary"
        disabled={loading}
        fullWidth
      >
        {loading ? "Ajout en cours..." : "Ajouter l'agent"}
      </Button>
    </Box>
  );
};

export default AgentForm;
