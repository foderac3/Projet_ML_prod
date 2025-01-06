# Utilisation de l'image Node.js pour builder l'application
FROM node:20 as build

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers
COPY . .

# Installer les dépendances et builder
RUN npm install && npm run build

# Utiliser Nginx pour servir l'application
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html

# Exposer le port 3000 pour le frontend
EXPOSE 3000
