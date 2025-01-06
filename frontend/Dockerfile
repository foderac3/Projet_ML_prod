# Étape 1 : Construire l'application Next.js
FROM node:20 as build

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY package*.json ./
COPY . .

# Installer les dépendances et builder
RUN npm install
RUN npm run build

# Vérification que le dossier .next existe
RUN ls -la /app/.next || (echo ".next directory not found" && exit 1)

# Étape 2 : Servir l'application avec Nginx
FROM nginx:alpine

# Copier les fichiers Next.js build vers Nginx
COPY --from=build /app/.next /usr/share/nginx/html/.next

# Ajouter la configuration par défaut de Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Exposer le port 3000
EXPOSE 3000

# Lancer Nginx
CMD ["nginx", "-g", "daemon off;"]
