# Étape 1 : Construction de l'environnement Python
FROM python:3.12-slim AS builder

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    wget \
    gcc \
    libpq-dev \
    --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Installer Dockerize pour la gestion des dépendances de démarrage
RUN wget https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz \
    && tar -C /usr/local/bin -xzf dockerize-linux-amd64-v0.6.1.tar.gz \
    && rm dockerize-linux-amd64-v0.6.1.tar.gz

# Copier uniquement les fichiers nécessaires pour installer les dépendances Python
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copier le code source de l'application
COPY . .

# Étape 2 : Création de l'image finale
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers depuis l'étape précédente
COPY --from=builder /app /app
COPY --from=builder /usr/local/bin/dockerize /usr/local/bin/dockerize

# Réinstaller les dépendances (sécurité pour l'image finale)
RUN pip install --no-cache-dir -r /app/requirements.txt

# Ajouter un utilisateur non-root pour plus de sécurité
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Exposer le port sur lequel le backend sera disponible
EXPOSE 8000

# Commande par défaut pour démarrer le backend
CMD ["dockerize", "-wait", "tcp://db:5432", "-wait", "tcp://redis:6379", "-timeout", "30s", \
    "python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
