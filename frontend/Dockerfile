# Étape 1 : Construire l'application Next.js
FROM node:20 as build

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers package.json et installer les dépendances
COPY package*.json ./
COPY . .

RUN npm install
RUN npm run build

# Vérifier si le build est bien généré
RUN ls -la /app/.next || (echo ".next directory not found" && exit 1)

# Étape 2 : Servir l'application avec Nginx
FROM nginx:alpine

# Copier le dossier Next.js build
COPY --from=build /app/.next /usr/share/nginx/html/.next

# Copier le dossier public (si présent)
COPY --from=build /app/public /usr/share/nginx/html || echo "No public folder found"

# Ajouter la configuration par défaut de Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]
