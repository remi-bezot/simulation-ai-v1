
from app.infrastructure.database.mongodb.collections import agents_collection, universes_collection

def reset_mongo_database():
    """Réinitialiser MongoDB."""
    agents_collection.delete_many({})
    universes_collection.delete_many({})
    print('Collections MongoDB réinitialisées.')

if __name__ == '__main__':
    reset_mongo_database()

