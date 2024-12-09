# Étape 1 : Construire l'application React
FROM node:18-alpine AS builder

# Définir le répertoire de travail pour la construction
WORKDIR /usr/src/app

# Copier les fichiers nécessaires pour installer les dépendances
COPY package.json yarn.lock ./

# Installer les dépendances en utilisant un fichier de verrouillage
RUN yarn install --frozen-lockfile

# Copier tout le code source de l'application React
COPY . .

# Construire l'application en mode production
RUN yarn build
