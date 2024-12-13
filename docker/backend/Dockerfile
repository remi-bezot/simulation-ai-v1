# Étape 1 : Construction de l'environnement Python
FROM python:3.12-slim AS builder

WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    wget \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Installer Dockerize pour gérer les dépendances entre conteneurs
RUN wget https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz \
    && tar -C /usr/local/bin -xzf dockerize-linux-amd64-v0.6.1.tar.gz \
    && rm dockerize-linux-amd64-v0.6.1.tar.gz

# Vérification de Dockerize
RUN dockerize --version

# Copier les dépendances Python
COPY ./src/backend/requirements.txt ./requirements.txt

# Installer les dépendances Python
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Vérification d'uvicorn
RUN python -m uvicorn --version || echo "uvicorn n'est pas installé correctement !"

# Copier le code source
COPY ./src/backend .

# Étape 2 : Création de l'image finale
FROM python:3.12-slim

WORKDIR /app

# Copier les fichiers depuis l'étape précédente
COPY --from=builder /app /app
COPY --from=builder /usr/local/bin/dockerize /usr/local/bin/dockerize

# Réinstaller les dépendances pour garantir leur disponibilité
RUN pip install --no-cache-dir -r /app/requirements.txt

# Vérifier la disponibilité d'uvicorn
RUN python -m uvicorn --version || echo "uvicorn n'est pas accessible dans l'étape finale !"

# Ajouter un utilisateur non-root
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Exposer le port pour le backend
EXPOSE 8000

# Commande pour démarrer le backend
CMD ["dockerize", "-wait", "tcp://db:5432", "-wait", "tcp://redis:6379", "-timeout", "30s", \
    "python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
