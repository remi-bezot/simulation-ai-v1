import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import {
  CssBaseline,
  AppBar,
  Toolbar,
  Button,
  Typography,
  Container,
} from "@mui/material";
import Dashboard from "./pages/dashboard/Dashboard";
import Worlds from "./pages/worlds/Worlds";
import Agents from "./pages/agents/Agents";
import Multiverse from "./pages/multiverse/Multiverse";
import Events from "./pages/events/Events";
import Home from "./pages/home/Home";
import NotFound from "./pages/notFound/NotFound";

const App = () => {
  return (
    <Router>
      {/* Réinitialisation des styles globaux */}
      <CssBaseline />

      {/* Barre de navigation */}
      <AppBar position="static" style={{ backgroundColor: "#1976d2" }}>
        <Toolbar>
          <Typography variant="h6" style={{ flexGrow: 1, textAlign: "left" }}>
            Simulation AI
          </Typography>
          <Button
            color="inherit"
            component={Link}
            to="/"
            style={{ textTransform: "none", marginLeft: "10px" }}
          >
            Accueil
          </Button>
          <Button
            color="inherit"
            component={Link}
            to="/dashboard"
            style={{ textTransform: "none", marginLeft: "10px" }}
          >
            Tableau de bord
          </Button>
          <Button
            color="inherit"
            component={Link}
            to="/worlds"
            style={{ textTransform: "none", marginLeft: "10px" }}
          >
            Mondes
          </Button>
          <Button
            color="inherit"
            component={Link}
            to="/agents"
            style={{ textTransform: "none", marginLeft: "10px" }}
          >
            Agents
          </Button>
          <Button
            color="inherit"
            component={Link}
            to="/multiverse"
            style={{ textTransform: "none", marginLeft: "10px" }}
          >
            Multivers
          </Button>
          <Button
            color="inherit"
            component={Link}
            to="/events"
            style={{ textTransform: "none", marginLeft: "10px" }}
          >
            Événements
          </Button>
        </Toolbar>
      </AppBar>

      {/* Contenu principal */}
      <Container
        maxWidth="lg"
        style={{
          marginTop: "30px",
          padding: "20px",
          backgroundColor: "#f5f5f5",
          borderRadius: "8px",
        }}
      >
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/worlds" element={<Worlds />} />
          <Route path="/agents" element={<Agents />} />
          <Route path="/multiverse" element={<Multiverse />} />
          <Route path="/events" element={<Events />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </Container>
    </Router>
  );
};

export default App;
