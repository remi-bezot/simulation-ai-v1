
from app.infrastructure.database.mongodb.collections import agents_collection

def seed_mongo_data():
    """Insérer des données initiales dans MongoDB."""
    agents_collection.insert_many([
        {'name': 'Agent Alpha', 'role': 'explorer'},
        {'name': 'Agent Beta', 'role': 'scientist'}
    ])
    print('Données initiales insérées dans MongoDB.')

if __name__ == '__main__':
    seed_mongo_data()

