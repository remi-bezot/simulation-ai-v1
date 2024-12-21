# Étape 1 : Utiliser une image Python légère
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers nécessaires pour installer les dépendances
COPY ../../src/backend/requirements.txt ./requirements.txt
COPY ./requirements-test.txt ./requirements-test.txt

# Installer les dépendances du backend et de test
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir -r requirements-test.txt

# Copier le code source du backend et les tests
COPY ../../src/backend ./backend
COPY . ./tests

# Ajouter un utilisateur non-root pour plus de sécurité
RUN useradd -m testuser && chown -R testuser:testuser /app
USER testuser

# Commande par défaut pour exécuter les tests
CMD ["pytest", "/app/tests"]
