# Utilise l'image officielle Redis basée sur Alpine pour une taille réduite
FROM redis:7-alpine

# Copier un fichier de configuration personnalisé si nécessaire
# COPY ./docker/redis/redis.conf /usr/local/etc/redis/redis.conf

# Exposer le port par défaut de Redis
EXPOSE 6379

# Commande par défaut pour démarrer Redis (utilisez une configuration personnalisée si nécessaire)
# CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]
CMD ["redis-server"]
