#!/bin/bash

# Chemin racine du projet
ROOT_DIR="./src/backend/app/infrastructure/database"

# Définir les répertoires à créer
declare -a DIRECTORIES=(
    "$ROOT_DIR/postgresql/migrations"
    "$ROOT_DIR/postgresql/scripts"
    "$ROOT_DIR/mongodb/scripts"
    "$ROOT_DIR/shared"
)

# Définir les fichiers à créer avec leur contenu
declare -A FILES_CONTENTS=(
    # PostgreSQL database.py
    ["$ROOT_DIR/postgresql/database.py"]="
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL_POSTGRESQL

# Configuration de l'engine PostgreSQL
engine = create_engine(DATABASE_URL_POSTGRESQL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    \"\"\"Obtenir une session PostgreSQL.\"\"\"
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
"

    # MongoDB database.py
    ["$ROOT_DIR/mongodb/database.py"]="
from pymongo import MongoClient
from app.config import DATABASE_URL_MONGODB

# Connexion MongoDB
client = MongoClient(DATABASE_URL_MONGODB)
db = client.get_database()  # Utilise la base spécifiée dans l'URL

def get_mongo_db():
    \"\"\"Obtenir la base MongoDB.\"\"\"
    return db
"

    # MongoDB collections.py
    ["$ROOT_DIR/mongodb/collections.py"]="
from app.infrastructure.database.mongodb.database import get_mongo_db

db = get_mongo_db()

agents_collection = db.get_collection('agents')
universes_collection = db.get_collection('universes')
"

    # PostgreSQL seed.py
    ["$ROOT_DIR/postgresql/scripts/seed.py"]="
from app.infrastructure.database.postgresql.database import SessionLocal
from app.core.models import Agent

def seed_postgres_data():
    \"\"\"Insérer des données initiales dans PostgreSQL.\"\"\"
    db = SessionLocal()
    try:
        agent1 = Agent(name='Agent Alpha', properties={'role': 'explorer'})
        agent2 = Agent(name='Agent Beta', properties={'role': 'scientist'})
        db.add_all([agent1, agent2])
        db.commit()
        print('Données initiales insérées dans PostgreSQL.')
    finally:
        db.close()

if __name__ == '__main__':
    seed_postgres_data()
"

    # MongoDB seed.py
    ["$ROOT_DIR/mongodb/scripts/seed.py"]="
from app.infrastructure.database.mongodb.collections import agents_collection

def seed_mongo_data():
    \"\"\"Insérer des données initiales dans MongoDB.\"\"\"
    agents_collection.insert_many([
        {'name': 'Agent Alpha', 'role': 'explorer'},
        {'name': 'Agent Beta', 'role': 'scientist'}
    ])
    print('Données initiales insérées dans MongoDB.')

if __name__ == '__main__':
    seed_mongo_data()
"

    # PostgreSQL reset.py
    ["$ROOT_DIR/postgresql/scripts/reset.py"]="
from app.infrastructure.database.postgresql.database import engine
from app.core.models import Base

def reset_postgres_database():
    \"\"\"Réinitialiser la base PostgreSQL.\"\"\"
    Base.metadata.drop_all(bind=engine)
    print('Base PostgreSQL réinitialisée.')

    Base.metadata.create_all(bind=engine)
    print('Tables PostgreSQL recréées.')

if __name__ == '__main__':
    reset_postgres_database()
"

    # MongoDB reset.py
    ["$ROOT_DIR/mongodb/scripts/reset.py"]="
from app.infrastructure.database.mongodb.collections import agents_collection, universes_collection

def reset_mongo_database():
    \"\"\"Réinitialiser MongoDB.\"\"\"
    agents_collection.delete_many({})
    universes_collection.delete_many({})
    print('Collections MongoDB réinitialisées.')

if __name__ == '__main__':
    reset_mongo_database()
"

    # Shared utils.py
    ["$ROOT_DIR/shared/utils.py"]="
import json

def to_json(data):
    \"\"\"Convertir des données Python en JSON.\"\"\"
    return json.dumps(data, indent=4, ensure_ascii=False)
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
