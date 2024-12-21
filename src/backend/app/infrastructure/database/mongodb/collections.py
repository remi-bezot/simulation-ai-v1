
from app.infrastructure.database.mongodb.database import get_mongo_db

db = get_mongo_db()

agents_collection = db.get_collection('agents')
universes_collection = db.get_collection('universes')

