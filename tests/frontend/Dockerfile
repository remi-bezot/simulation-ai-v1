# Étape 1 : Utiliser une image Node.js légère
FROM node:18-alpine

# Étape 2 : Définir le répertoire de travail
WORKDIR /usr/src/app

# Étape 3 : Copier les fichiers nécessaires pour les dépendances
COPY src/frontend/package.json src/frontend/yarn.lock ./

# Étape 4 : Installer les dépendances
RUN yarn install \
    && yarn add @babel/core @babel/preset-env @babel/preset-react @babel/preset-typescript babel-jest jest jsdom @types/jest @types/jsdom

# Étape 5 : Copier le code source et les configurations nécessaires
COPY src/frontend ./src
COPY tests/frontend/babel.config.js ./babel.config.js
COPY tests/frontend/jest.config.js ./jest.config.js
COPY src/frontend/tsconfig.json ./tsconfig.json

# Étape 6 : Copier les tests
COPY tests/frontend ./tests

# Étape 7 : Définir la commande par défaut pour exécuter les tests
CMD ["yarn", "jest", "--config", "jest.config.js"]
