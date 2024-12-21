
from pymongo import MongoClient
from app.config import DATABASE_URL_MONGODB

# Connexion MongoDB
client = MongoClient(DATABASE_URL_MONGODB)
db = client.get_database()  # Utilise la base spécifiée dans l'URL

def get_mongo_db():
    """Obtenir la base MongoDB."""
    return db

