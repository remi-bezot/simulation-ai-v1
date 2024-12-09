# Utilise l'image officielle PostgreSQL
FROM postgres:15

# Copier les fichiers de configuration
COPY init.sql /docker-entrypoint-initdb.d/

# Exposer le port
EXPOSE 5432
