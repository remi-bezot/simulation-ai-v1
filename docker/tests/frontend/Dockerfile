# Étape 1 : Utiliser une image Node.js légère
FROM node:18-alpine

# Étape 2 : Définir le répertoire de travail
WORKDIR /usr/src/app

# Étape 3 : Copier les fichiers nécessaires pour installer les dépendances
COPY ./src/frontend/package.json ./src/frontend/yarn.lock ./

# Étape 4 : Installer les dépendances
RUN yarn install --frozen-lockfile \
    && yarn add @babel/core @babel/preset-env @babel/preset-react @babel/preset-typescript \
    babel-jest jest jsdom @types/jest @types/jsdom

# Étape 5 : Copier le code source et les configurations nécessaires
COPY ./src/frontend ./src
COPY ./src/frontend/tsconfig.json ./tsconfig.json

# Étape 6 : Copier les configurations Babel et Jest, ainsi que les tests
COPY ./babel.config.js ./babel.config.js
COPY ./jest.config.js ./jest.config.js
COPY ./tests ./tests

# Étape 7 : Définir un utilisateur non-root pour plus de sécurité
RUN adduser --disabled-password appuser && chown -R appuser:appuser /usr/src/app
USER appuser

# Étape 8 : Définir la commande par défaut pour exécuter les tests
CMD ["yarn", "jest", "--config", "jest.config.js"]
