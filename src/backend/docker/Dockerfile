# Utilisez une image de base Python 3.10
FROM python:3.12-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les dépendances
COPY ../requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY ../app /app/app

# Exposer le port utilisé par FastAPI
EXPOSE 8000

# Lancer l'application avec Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
