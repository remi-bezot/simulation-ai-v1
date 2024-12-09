# Étape 1 : Utiliser une image Python légère
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Copier et installer les dépendances Python
COPY ./tests/backend/requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copier le code source et les tests dans le conteneur
COPY ./src/backend /app/backend
COPY ./tests/backend /app/tests

# Définir les variables d'environnement pour les tests (si nécessaire)
# ENV DATABASE_URL="postgresql://user:password@db:5432/test_db"

# Ajouter un utilisateur non-root pour la sécurité
RUN useradd -m testuser
USER testuser

# Commande par défaut pour exécuter les tests
CMD ["pytest", "/app/tests"]
