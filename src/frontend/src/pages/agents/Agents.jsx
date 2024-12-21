
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

