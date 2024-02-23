#!/bin/bash

check_failure() {
    if [ $? -ne 0 ]; then
        echo -e "\e[91mErreur: $1\e[0m"
        exit 1
    fi
}

echo_success() {
    echo -e "\e[92;1m$1\e[0m"
}

echo "Arrêt du service postgresql..."
sudo systemctl stop postgresql
check_failure "Échec de l'arrêt du service postgresql"
echo_success "Arrêt du service postgresql effectué avec succès"

echo "Arrêt du serveur web local..."
sudo systemctl stop apache2
check_failure "Échec de l'arrêt du serveur web"
echo_success "Arrêt du service apache2 effectué avec succès"

echo "Suppression des éventuels conteneurs déjà créés..."
docker rmi isla_aiguilleur:latest isla_controleur_db:latest isla_choix:latest

echo "Suppression de l'éventuel network docker déjà créé..."
docker network rm isla_network

echo "Création du network..."
docker network create --subnet=172.25.0.0/16 isla_network
check_failure "Échec de la création du network"
echo_success "Network créé avec succès"

echo "Création des images définitives..."
cd aiguilleur
docker build -t isla_aiguilleur:latest -f Dockerfile .
check_failure "Échec de la création de l'image isla_aiguilleur"
echo_success "Image api_ema_postgress_configurator créée avec succès"
cd ../

cd controleur_db
docker build -t isla_controleur_db:latest -f Dockerfile .
check_failure "Échec de la création de l'image isla_controleur_db"
echo_success "Image api_ema_postgress_configurator créée avec succès"
cd ../

cd choix
docker build -t isla_choix:latest -f Dockerfile .
check_failure "Échec de la création de l'image isla_choix"
echo_success "Image api_ema_postgress_configurator créée avec succès"
cd ../

echo_success "Initialisation exécutée avec succès."
echo "Vous pouvez maintenant exécuter la commande : docker-compose up"

