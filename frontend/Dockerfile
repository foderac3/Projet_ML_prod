# Étape 1 : Construire l'application Next.js
FROM node:20 as build

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires et installer les dépendances
COPY package*.json ./
COPY . .

RUN npm install
RUN npm run build

# Vérification du dossier public (ajout d'un fichier vide si nécessaire)
RUN mkdir -p /app/public && echo "Placeholder for public folder" > /app/public/index.html

# Étape 2 : Servir avec Nginx
FROM nginx:alpine

# Copier le dossier Next.js build
COPY --from=build /app/.next /usr/share/nginx/html/.next

# Copier le dossier public (il existera toujours après la vérification)
COPY --from=build /app/public /usr/share/nginx/html

# Ajouter la configuration Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]
