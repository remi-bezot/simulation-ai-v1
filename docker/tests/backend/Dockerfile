# Étape 1 : Utiliser une image Python légère comme base
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copier les dépendances Python pour le backend
COPY ../src/backend/requirements.txt ./requirements.txt

# Installer les dépendances Python pour le backend
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copier les dépendances spécifiques aux tests
COPY ./requirements-test.txt ./requirements-test.txt

# Installer les dépendances pour les tests
RUN pip install --no-cache-dir -r requirements-test.txt

# Copier uniquement le code source et les tests
COPY ../src/backend ./backend
COPY . ./tests

# Ajouter un utilisateur non-root pour des raisons de sécurité
RUN useradd -m testuser && chown -R testuser:testuser /app
USER testuser

# Exposer un port pour les tests si nécessaire (par exemple pour les tests d'intégration)
EXPOSE 8000

# Commande par défaut pour exécuter les tests backend
CMD ["pytest", "/app/tests"]
