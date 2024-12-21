import React, { useState } from "react";
import {
  Box,
  Button,
  Slider,
  Typography,
  TextField,
  Alert,
} from "@mui/material";

interface SimulationControlsProps {
  onStart: () => void;
  onStop: () => void;
  onReset: () => void;
  onSpeedChange: (speed: number) => void;
  onAddSphere: (name: string, color: string) => void;
  onRemoveSphere: () => void;
}

const SimulationControls: React.FC<SimulationControlsProps> = ({
  onStart,
  onStop,
  onReset,
  onSpeedChange,
  onAddSphere,
  onRemoveSphere,
}) => {
  const [speed, setSpeed] = useState<number>(1);
  const [sphereName, setSphereName] = useState<string>("");
  const [sphereColor, setSphereColor] = useState<string>("#007bff");
  const [error, setError] = useState<string | null>(null);

  const handleSpeedChange = (_: Event, value: number | number[]) => {
    if (typeof value === "number") {
      setSpeed(value);
      onSpeedChange(value); // Transmet la nouvelle vitesse au parent
    }
  };

  const handleAddSphere = () => {
    if (sphereName.trim()) {
      if (!/^#[0-9A-F]{6}$/i.test(sphereColor)) {
        setError(
          "Veuillez entrer une couleur hexadécimale valide (ex. #FF5733)."
        );
        return;
      }
      onAddSphere(sphereName, sphereColor); // Ajoute une sphère via le parent
      setSphereName(""); // Réinitialise le champ après l'ajout
      setSphereColor("#007bff"); // Réinitialise la couleur
      setError(null); // Réinitialise les erreurs
    }
  };

  const handleReset = () => {
    onReset();
    setSpeed(1); // Réinitialise la vitesse à la valeur par défaut
  };

  return (
    <Box
      display="flex"
      flexDirection="column"
      alignItems="center"
      justifyContent="center"
      gap={2}
      padding={2}
      style={{
        border: "1px solid #ddd",
        borderRadius: "8px",
        backgroundColor: "#f5f5f5",
        marginTop: "20px",
      }}
    >
      <Typography variant="h6">Contrôles de la simulation</Typography>

      <Box display="flex" gap={2}>
        <Button variant="contained" color="primary" onClick={onStart}>
          Démarrer
        </Button>
        <Button variant="contained" color="secondary" onClick={onStop}>
          Arrêter
        </Button>
        <Button variant="outlined" onClick={handleReset}>
          Réinitialiser
        </Button>
      </Box>

      <Box width="80%" marginTop={2}>
        <Typography variant="body2">
          Vitesse de simulation : {speed.toFixed(1)}x
        </Typography>
        <Slider
          aria-label="Vitesse de simulation"
          defaultValue={1}
          min={0.1}
          max={5}
          step={0.1}
          onChange={handleSpeedChange}
          value={speed}
          valueLabelDisplay="auto"
        />
      </Box>

      {error && (
        <Alert severity="error" style={{ marginTop: "10px" }}>
          {error}
        </Alert>
      )}

      <Box
        width="80%"
        marginTop={2}
        display="flex"
        flexDirection="column"
        gap={1}
      >
        <Typography variant="body2">Ajouter une nouvelle sphère :</Typography>
        <TextField
          label="Nom de la sphère"
          variant="outlined"
          size="small"
          value={sphereName}
          onChange={(e) => setSphereName(e.target.value)}
          aria-label="Nom de la sphère"
        />
        <TextField
          label="Couleur de la sphère (hex)"
          variant="outlined"
          size="small"
          type="color"
          value={sphereColor}
          onChange={(e) => setSphereColor(e.target.value)}
          aria-label="Couleur de la sphère"
        />
        <Button
          variant="contained"
          color="primary"
          onClick={handleAddSphere}
          disabled={!sphereName.trim()}
        >
          Ajouter une sphère
        </Button>
      </Box>

      <Button variant="outlined" color="error" onClick={onRemoveSphere}>
        Supprimer une sphère
      </Button>
    </Box>
  );
};

export default SimulationControls;
