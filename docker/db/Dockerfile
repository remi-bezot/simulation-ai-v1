# Utilise l'image officielle PostgreSQL
FROM postgres:15

# Copier les fichiers d'initialisation
COPY ./docker/db/init.sql /docker-entrypoint-initdb.d/

# Définir les variables d'environnement pour configurer la base de données
ENV POSTGRES_USER=default_user
ENV POSTGRES_PASSWORD=default_password
ENV POSTGRES_DB=default_db

# Exposer le port par défaut de PostgreSQL
EXPOSE 5432
