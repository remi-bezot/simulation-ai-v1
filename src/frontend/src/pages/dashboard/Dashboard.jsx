import React, { useEffect, useState } from "react";
import { get } from "../../services/api";
import {
  Box,
  Typography,
  CircularProgress,
  Paper,
  Button,
} from "@mui/material";
import {
  LineChart,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

// Composant réutilisable pour afficher des états de chargement ou des erreurs
const CenteredBox = ({ children }) => (
  <Box
    display="flex"
    justifyContent="center"
    alignItems="center"
    height="100vh"
    bgcolor="#f9f9f9"
  >
    {children}
  </Box>
);

const Dashboard = () => {
  const [chartData, setChartData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchData = async () => {
    setLoading(true);
    setError(null);
    try {
      const result = await get("/api/dashboard");
      setChartData(result);
    } catch (err) {
      console.error("Erreur de récupération des données :", err);
      setError("Impossible de récupérer les données.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  if (loading) {
    return (
      <CenteredBox>
        <CircularProgress />
      </CenteredBox>
    );
  }

  if (error) {
    return (
      <CenteredBox>
        <Typography color="error">{error}</Typography>
      </CenteredBox>
    );
  }

  if (!chartData || chartData.length === 0) {
    return (
      <CenteredBox>
        <Typography>Aucune donnée disponible</Typography>
      </CenteredBox>
    );
  }

  return (
    <Box padding={3}>
      <Box display="flex" justifyContent="space-between" alignItems="center">
        <Typography variant="h4" gutterBottom>
          Tableau de bord - Statistiques
        </Typography>
        <Button variant="contained" onClick={fetchData} disabled={loading}>
          {loading ? "Chargement..." : "Rafraîchir les données"}
        </Button>
      </Box>
      <Paper
        elevation={3}
        sx={{
          padding: "20px",
          marginBottom: "20px",
          backgroundColor: "#f9f9f9",
        }}
      >
        <ResponsiveContainer width="100%" height={300}>
          <LineChart
            data={chartData}
            margin={{ top: 20, right: 30, bottom: 20, left: 0 }}
          >
            <CartesianGrid stroke="#e0e0e0" />
            <XAxis dataKey="name" tick={{ fontSize: 14, fill: "#888" }} />
            <YAxis tick={{ fontSize: 14, fill: "#888" }} />
            <Tooltip />
            <Line type="monotone" dataKey="value" stroke="#007bff" strokeWidth={3} />
          </LineChart>
        </ResponsiveContainer>
      </Paper>
    </Box>
  );
};

export default Dashboard;
