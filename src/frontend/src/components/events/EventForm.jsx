import React, { useState } from "react";
import { post } from "../../services/api";
import { Box, TextField, Button, Typography } from "@mui/material";

const EventForm = ({ onEventAdded }) => {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      await post("/api/events", { name, description });
      setName("");
      setDescription("");
      onEventAdded();
    } catch (err) {
      console.error("Erreur lors de l'ajout de l'événement :", err);
      setError("Impossible d'ajouter l'événement.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box component="form" onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
      <Typography variant="h6" gutterBottom>
        Ajouter un nouvel événement
      </Typography>
      {error && <Typography color="error">{error}</Typography>}
      <TextField
        label="Nom de l'événement"
        value={name}
        onChange={(e) => setName(e.target.value)}
        fullWidth
        required
        style={{ marginBottom: "10px" }}
      />
      <TextField
        label="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        fullWidth
        multiline
        rows={3}
        style={{ marginBottom: "10px" }}
      />
      <Button
        type="submit"
        variant="contained"
        color="primary"
        disabled={loading}
        fullWidth
      >
        {loading ? "Ajout en cours..." : "Ajouter l'événement"}
      </Button>
    </Box>
  );
};

export default EventForm;
