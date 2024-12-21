import React from "react";
import { Card, CardContent, Typography } from "@mui/material";

const AgentList = ({ agents }) => {
  if (!agents || agents.length === 0) {
    return <Typography>Aucun agent disponible.</Typography>;
  }

  return (
    <div style={{ display: "flex", flexWrap: "wrap", gap: "20px" }}>
      {agents.map((agent) => (
        <Card
          key={agent.id}
          style={{
            width: "250px",
            padding: "10px",
            textAlign: "center",
            backgroundColor: "#f5f5f5",
            borderRadius: "8px",
          }}
        >
          <CardContent>
            <Typography variant="h6">{agent.name}</Typography>
            <Typography variant="body2">
              {agent.properties
                ? `Propriétés : ${JSON.stringify(agent.properties)}`
                : "Pas de propriétés"}
            </Typography>
          </CardContent>
        </Card>
      ))}
    </div>
  );
};

export default AgentList;
