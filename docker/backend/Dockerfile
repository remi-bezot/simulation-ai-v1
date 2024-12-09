# Étape 1 : Construire l'environnement
FROM python:3.12-slim AS builder

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    wget gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Télécharger et installer Dockerize
RUN wget https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz \
    && tar -C /usr/local/bin -xzf dockerize-linux-amd64-v0.6.1.tar.gz \
    && chmod +x /usr/local/bin/dockerize \
    && rm dockerize-linux-amd64-v0.6.1.tar.gz

# Ajouter le PATH pour les binaires Python utilisateur
ENV PATH="/root/.local/bin:$PATH"

# Copier les dépendances Python
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Étape 2 : Créer l'image de production
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les dépendances de l'étape précédente
COPY --from=builder /app /app

# Copier Dockerize depuis l'étape de build
COPY --from=builder /usr/local/bin/dockerize /usr/local/bin/dockerize

# Ajouter le PATH pour les binaires Python utilisateur
ENV PATH="/root/.local/bin:$PATH"

# Copier le code source
COPY . .

# Ajouter un utilisateur non-root pour la sécurité
RUN useradd -m appuser
USER appuser

# Exposer le port pour l'API
EXPOSE 8000

# Commande par défaut
CMD ["dockerize", "-wait", "tcp://db:5432", "-wait", "tcp://redis:6379", "-timeout", "30s", \
    "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
