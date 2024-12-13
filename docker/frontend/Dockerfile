# Étape 1 : Construire l'application React
FROM node:18-alpine AS builder

WORKDIR /app

# Copier les fichiers nécessaires pour installer les dépendances
COPY ./src/frontend/package.json ./package.json
COPY ./src/frontend/yarn.lock ./yarn.lock
COPY ./src/frontend/tsconfig.json ./tsconfig.json
COPY ./src/frontend/craco.config.js ./craco.config.js

# Installer les dépendances
RUN yarn install --frozen-lockfile

# Copier tout le code source
COPY ./src/frontend ./

# Construire l'application
RUN yarn build

# Étape 2 : Serveur Nginx pour servir l'application
FROM nginx:stable-alpine

# Supprimer les fichiers par défaut d'Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copier les fichiers de build depuis l'étape précédente
COPY --from=builder /app/build /usr/share/nginx/html

# Copier la configuration Nginx personnalisée
COPY ./docker/nginx/nginx.conf /etc/nginx/nginx.conf

# Exposer le port utilisé par Nginx
EXPOSE 80

# Commande par défaut pour démarrer Nginx
CMD ["nginx", "-g", "daemon off;"]
