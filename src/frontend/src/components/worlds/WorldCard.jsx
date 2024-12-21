import React from "react";
import { Card, CardContent, Typography } from "@mui/material";

const WorldCard = ({ world }) => {
  return (
    <Card
      style={{
        margin: "10px",
        padding: "10px",
        textAlign: "center",
        backgroundColor: "#f5f5f5",
        borderRadius: "8px",
      }}
    >
      <CardContent>
        <Typography variant="h6">{world.name || "Nom indisponible"}</Typography>
        {world.properties ? (
          <Typography variant="body2">
            Propriétés : {JSON.stringify(world.properties)}
          </Typography>
        ) : (
          <Typography variant="body2">
            <em>Aucune propriété disponible</em>
          </Typography>
        )}
      </CardContent>
    </Card>
  );
};

export default WorldCard;
