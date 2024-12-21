#!/bin/bash

# Chemin racine du projet
ROOT_DIR="./src/frontend/src"

# Définir les répertoires à créer
declare -a DIRECTORIES=(
    "$ROOT_DIR/pages/dashboard"
    "$ROOT_DIR/pages/worlds"
    "$ROOT_DIR/pages/agents"
    "$ROOT_DIR/pages/multiverse"
    "$ROOT_DIR/pages/events"
    "$ROOT_DIR/pages/home"
    "$ROOT_DIR/pages/notFound"
    "$ROOT_DIR/components/dashboard"
    "$ROOT_DIR/components/worlds"
    "$ROOT_DIR/components/agents"
    "$ROOT_DIR/components/multiverse"
    "$ROOT_DIR/components/events"
    "$ROOT_DIR/components"
    "$ROOT_DIR/services"
)

# Définir les fichiers à créer avec leur contenu
declare -A FILES_CONTENTS=(
    ["$ROOT_DIR/pages/dashboard/Dashboard.jsx"]="
import React from 'react';
import StatsChart from '../../components/dashboard/StatsChart';
import SummaryCard from '../../components/dashboard/SummaryCard';
import { Box, Typography, Grid } from '@mui/material';

const Dashboard = () => {
    return (
        <Box padding={3}>
            <Typography variant='h4' gutterBottom>
                Tableau de bord
            </Typography>
            <Grid container spacing={3}>
                <Grid item xs={12} md={6}>
                    <SummaryCard title='Statistiques clés' value='1234' />
                </Grid>
                <Grid item xs={12} md={6}>
                    <StatsChart />
                </Grid>
            </Grid>
        </Box>
    );
};

export default Dashboard;
"

    ["$ROOT_DIR/pages/worlds/Worlds.jsx"]="
import React, { useEffect, useState } from 'react';
import WorldList from '../../components/worlds/WorldList';
import Loader from '../../components/Loader';
import { Box, Typography } from '@mui/material';
import { get } from '../../services/api';

const Worlds = () => {
    const [worlds, setWorlds] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await get('/api/worlds');
                setWorlds(response.worlds);
            } catch (err) {
                setError('Erreur de chargement.');
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, []);

    if (loading) return <Loader />;
    if (error) return <Typography color='error'>{error}</Typography>;

    return (
        <Box>
            <Typography variant='h4' gutterBottom>
                Liste des Mondes
            </Typography>
            <WorldList worlds={worlds} />
        </Box>
    );
};

export default Worlds;
"

    ["$ROOT_DIR/pages/agents/Agents.jsx"]="
import React, { useEffect, useState } from 'react';
import AgentList from '../../components/agents/AgentList';
import AgentForm from '../../components/agents/AgentForm';
import Loader from '../../components/Loader';
import { Box, Typography, Button } from '@mui/material';
import { get } from '../../services/api';

const Agents = () => {
    const [agents, setAgents] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [showForm, setShowForm] = useState(false);

    useEffect(() => {
        const fetchAgents = async () => {
            try {
                const response = await get('/api/agents');
                setAgents(response.agents);
            } catch (err) {
                setError('Erreur lors de la récupération des agents.');
            } finally {
                setLoading(false);
            }
        };
        fetchAgents();
    }, []);

    if (loading) return <Loader />;
    if (error) return <Typography color='error'>{error}</Typography>;

    return (
        <Box>
            <Typography variant='h4' gutterBottom>
                Liste des Agents
            </Typography>
            <Button
                variant='contained'
                onClick={() => setShowForm(!showForm)}
                style={{ marginBottom: '10px' }}
            >
                {showForm ? 'Annuler' : 'Ajouter un agent'}
            </Button>
            {showForm && <AgentForm />}
            <AgentList agents={agents} />
        </Box>
    );
};

export default Agents;
"

    ["$ROOT_DIR/components/dashboard/StatsChart.jsx"]="
import React from 'react';
import { Box, Typography } from '@mui/material';

const StatsChart = () => {
    return (
        <Box>
            <Typography variant='body1'>Graphique des statistiques</Typography>
        </Box>
    );
};

export default StatsChart;
"

    ["$ROOT_DIR/components/worlds/WorldList.jsx"]="
import React from 'react';
import WorldCard from './WorldCard';
import { Paper } from '@mui/material';

const WorldList = ({ worlds }) => {
    return (
        <Paper elevation={3} style={{ padding: '20px' }}>
            {worlds.map((world) => (
                <WorldCard key={world.id} world={world} />
            ))}
        </Paper>
    );
};

export default WorldList;
"

    ["$ROOT_DIR/services/api.js"]="
export const get = async (url) => {
    const response = await fetch(\`http://localhost:8000\${url}\`);
    if (!response.ok) {
        throw new Error(\`Erreur HTTP \${response.status}\`);
    }
    return response.json();
};
"
)

# Création des répertoires
echo "Création des répertoires..."
for dir in "${DIRECTORIES[@]}"; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        echo "Dossier créé : $dir"
    else
        echo "Dossier déjà existant : $dir"
    fi
done

# Création des fichiers avec contenu
echo "Création des fichiers..."
for filepath in "${!FILES_CONTENTS[@]}"; do
    if [ ! -f "$filepath" ]; then
        echo -e "${FILES_CONTENTS[$filepath]}" > "$filepath"
        echo "Fichier créé : $filepath"
    else
        echo "Fichier déjà existant : $filepath"
    fi
done

echo "Structure complète générée avec succès."
