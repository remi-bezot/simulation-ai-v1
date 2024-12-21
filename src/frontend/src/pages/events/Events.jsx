import React, { useEffect, useState } from "react";
import EventForm from "../../components/events/EventForm";
import Loader from "../../components/Loader";
import { Box, Typography, Paper } from "@mui/material";
import { get } from "../../services/api";

const Events = () => {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchEvents = async () => {
    try {
      const response = await get("/api/events");
      setEvents(response.events);
    } catch (err) {
      setError("Erreur lors de la récupération des événements.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchEvents();
  }, []);

  if (loading) {
    return <Loader />;
  }

  if (error) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center" height="100vh">
        <Typography color="error">{error}</Typography>
      </Box>
    );
  }

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Gestion des Événements
      </Typography>
      <EventForm onEventAdded={fetchEvents} />
      <Paper elevation={3} style={{ padding: "20px", marginTop: "20px" }}>
        {events.length > 0 ? (
          events.map((event, index) => (
            <Typography key={index} style={{ marginBottom: "10px" }}>
              {event.name} - {event.description || "Pas de description"}
            </Typography>
          ))
        ) : (
          <Typography>Aucun événement trouvé.</Typography>
        )}
      </Paper>
    </Box>
  );
};

export default Events;
