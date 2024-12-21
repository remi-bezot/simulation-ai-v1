import React from "react";
import { Typography, Box, Card, CardContent } from "@mui/material";

const SimulationStats = ({ data }) => {
  if (!data || data.length === 0) {
    return (
      <Box marginTop={3} textAlign="center">
        <Typography variant="h6" color="textSecondary">
          Aucune donnée disponible pour afficher les statistiques.
        </Typography>
      </Box>
    );
  }

  return (
    <Box marginTop={3}>
      <Typography variant="h5" gutterBottom>
        Statistiques
      </Typography>
      <Box display="flex" flexWrap="wrap" gap={2}>
        {data.map((item, index) => (
          <Card
            key={index}
            style={{
              width: "250px",
              border: "1px solid #ddd",
              borderRadius: "8px",
              backgroundColor: "#f9f9f9",
            }}
          >
            <CardContent>
              <Typography variant="h6">{item.name || "Nom indisponible"}</Typography>
              <Typography variant="body2" color="textSecondary">
                {item.description || "Pas de description"}
              </Typography>
              {item.properties && (
                <Typography variant="body2" style={{ marginTop: "10px" }}>
                  Propriétés : {JSON.stringify(item.properties)}
                </Typography>
              )}
            </CardContent>
          </Card>
        ))}
      </Box>
    </Box>
  );
};

export default SimulationStats;
