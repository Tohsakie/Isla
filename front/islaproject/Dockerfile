# Utilisation d'une image de node.js comme base
FROM node:latest as build-stage

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires
COPY package*.json ./

# Installer les dépendances
RUN npm install

# Copier tous les fichiers du projet dans le répertoire de travail
COPY . .

# Construire l'application Vue.js pour la production
RUN npm install -g vite

RUN npm run build

# Utiliser une image légère nginx pour servir l'application construite
FROM nginx:latest

# Copier les fichiers de l'étape de construction précédente dans le répertoire de travail de nginx
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Exposer le port 80 pour accéder à l'application via HTTP
EXPOSE 80

# Commande pour démarrer nginx lorsqu'un conteneur basé sur cette image est lancé
CMD ["nginx", "-g", "daemon off;"]
