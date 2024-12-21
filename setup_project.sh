#!/bin/bash

# Chemin racine du projet
ROOT_DIR="."

# Définir les répertoires à créer
declare -a DIRECTORIES=(
    "$ROOT_DIR/src/backend/app/application/services"
    "$ROOT_DIR/src/backend/app/application/use_cases"
    "$ROOT_DIR/src/backend/app/core/agents/actions"
    "$ROOT_DIR/src/backend/app/core/agents/behaviors"
    "$ROOT_DIR/src/backend/app/core/agents/types"
    "$ROOT_DIR/src/backend/app/core/events"
    "$ROOT_DIR/src/backend/app/core/multiverse"
    "$ROOT_DIR/src/backend/app/core/resources"
    "$ROOT_DIR/src/backend/app/infrastructure/database/migrations"
    "$ROOT_DIR/src/backend/app/infrastructure/database/scripts"
    "$ROOT_DIR/src/backend/app/infrastructure/messaging"
    "$ROOT_DIR/src/backend/app/infrastructure/monitoring"
    "$ROOT_DIR/src/backend/app/infrastructure/storage"
    "$ROOT_DIR/src/backend/app/routers"
    "$ROOT_DIR/src/backend/tests"
    "$ROOT_DIR/src/frontend/src/components"
    "$ROOT_DIR/src/frontend/src/services"
    "$ROOT_DIR/src/frontend/src/styles"
    "$ROOT_DIR/src/frontend/public"
    "$ROOT_DIR/docs"
    "$ROOT_DIR/scripts"
)

# Définir les fichiers à créer avec leur contenu complet
declare -A FILES_CONTENTS=(
    # Backend main.py
    ["$ROOT_DIR/src/backend/app/main.py"]="
from fastapi import FastAPI
from app.routers import agents_router, multiverse_router, dashboard_router, world_router, events_router

app = FastAPI(title='Simulation AI', version='1.3.0')

# Inclusion des routers
app.include_router(agents_router.router, prefix='/api/agents', tags=['Agents'])
app.include_router(multiverse_router.router, prefix='/api/multiverse', tags=['Multiverse'])
app.include_router(dashboard_router.router, prefix='/api/dashboard', tags=['Dashboard'])
app.include_router(world_router.router, prefix='/api/worlds', tags=['Worlds'])
app.include_router(events_router.router, prefix='/api/events', tags=['Events'])

@app.get('/')
def root():
    return {'message': 'Welcome to Simulation AI'}

@app.get('/health')
def health_check():
    return {'status': 'ok', 'version': '1.3.0', 'uptime': '100 hours'}
"
    # Backend world_router.py
    ["$ROOT_DIR/src/backend/app/routers/world_router.py"]="
from fastapi import APIRouter
from app.application.services.world_service import list_worlds, create_world

router = APIRouter(prefix='/worlds', tags=['Worlds'])

@router.get('/')
def get_worlds():
    return list_worlds()

@router.post('/')
def add_world(world: dict):
    return create_world(world)
"
    # Backend events_router.py
    ["$ROOT_DIR/src/backend/app/routers/events_router.py"]="
from fastapi import APIRouter
from app.application.services.event_service import EventManager

router = APIRouter()

event_manager = EventManager()

@router.post('/trigger')
def trigger_event(event_name: str):
    return event_manager.trigger_event(event_name)
"
    # Backend world_service.py
    ["$ROOT_DIR/src/backend/app/application/services/world_service.py"]="
_worlds = []  # Temporary storage

def list_worlds():
    return {'worlds': _worlds}

def create_world(data):
    new_world = {'id': len(_worlds) + 1, 'name': data.get('name'), 'properties': data.get('properties')}
    _worlds.append(new_world)
    return {'message': 'World created', 'world': new_world}
"
    # Backend agent_service.py
    ["$ROOT_DIR/src/backend/app/application/services/agent_service.py"]="
def get_agents():
    return ['Agent 1', 'Agent 2']

def create_agent(name):
    return {'message': f'Agent {name} created successfully'}
"
    # Backend tests/test_worlds.py
    ["$ROOT_DIR/src/backend/tests/test_worlds.py"]="
import pytest
from fastapi.testclient import TestClient
from src.backend.app.main import app

client = TestClient(app)

def test_get_worlds():
    response = client.get('/api/worlds/')
    assert response.status_code == 200
    assert 'worlds' in response.json()

def test_create_world():
    response = client.post('/api/worlds/', json={'name': 'Test World'})
    assert response.status_code == 200
    assert response.json()['message'] == 'World created'
"
    # Frontend App.jsx
    ["$ROOT_DIR/src/frontend/src/components/App.jsx"]="
import React from 'react';
import GlobalStyles from '../styles/globalStyles';
import Dashboard from './Dashboard';

function App() {
    return (
        <>
            <GlobalStyles />
            <div>
                <h1>Simulation Dashboard</h1>
                <Dashboard />
            </div>
        </>
    );
}

export default App;
"
    # Frontend Dashboard.jsx
    ["$ROOT_DIR/src/frontend/src/components/Dashboard.jsx"]="
import React from 'react';

function Dashboard({ worlds }) {
    return (
        <div>
            <h2>World List</h2>
            <ul>
                {worlds.map((world, index) => (
                    <li key={index}>{world.name}</li>
                ))}
            </ul>
        </div>
    );
}

export default Dashboard;
"
    # Documentation README.md
    ["$ROOT_DIR/docs/README.md"]="
# Simulation AI

Simulation AI is a modular framework designed to simulate agents, resources, and multiverses.

## Features
- **Agent Management**: Create and manage agents with customizable behaviors.
- **Event Triggering**: Manage global and local events dynamically.
- **Dashboard**: Intuitive React-based frontend for visualization.

## Setup Instructions
1. Install backend dependencies:
   \`pip install -r requirements.txt\`
2. Install frontend dependencies:
   \`npm install\`
3. Run the backend:
   \`uvicorn app.main:app --reload\`
4. Run the frontend:
   \`npm start\`
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

# Création des fichiers avec contenu enrichi
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
