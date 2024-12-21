import os

# Configuration pour PostgreSQL
DATABASE_URL_POSTGRESQL = os.getenv(
    "DATABASE_URL_POSTGRESQL",
    "postgresql://username:password@localhost:5432/simulation_ai",
)

# Configuration pour MongoDB
DATABASE_URL_MONGODB = os.getenv(
    "DATABASE_URL_MONGODB", "mongodb://localhost:27017/simulation_ai"
)

# Autres configurations globales
SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    "https://monfrontend.com",
]
