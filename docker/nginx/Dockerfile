# Étape 2 : Serveur Nginx pour servir l'application
FROM nginx:stable-alpine

# Supprimer les fichiers par défaut d'Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copier les fichiers de build depuis l'étape précédente
COPY --from=builder /usr/src/app/build /usr/share/nginx/html

# Copier la configuration Nginx personnalisée
COPY ./docker/nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./docker/nginx/conf.d /etc/nginx/conf.d

# Exposer le port utilisé par Nginx
EXPOSE 80

# Commande par défaut pour démarrer Nginx
CMD ["nginx", "-g", "daemon off;"]
