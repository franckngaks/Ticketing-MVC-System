🎧 Helpline Management System (Architecture MVC)

📝 Présentation du Projet

Ce projet est une application de gestion de tickets d'incidents et de référentiel employés, développée en Python avec une architecture MVC (Modèle-Vue-Contrôleur). Il a été conçu pour répondre aux besoins de maintenance applicative et de support technique.

🚀 Fonctionnalités

Gestion des Employés (Service Identity) : CRUD complet (Création, Lecture, Mise à jour, Suppression).

Gestion des Incidents (Service Ticketing) : Workflow de création, modification et résolution de tickets.

Persistence SQL : Base de données relationnelle MySQL (via PHPMyAdmin).

Logique Métier : Validation des rôles (Tech/Admin) et intégrité des données.

🏗️ Architecture Technique

Le projet respecte une séparation stricte des responsabilités pour garantir la maintenabilité :

model/ : Définition des entités (objets Python).

repository/ : Couche d'accès aux données (Requêtes SQL pures).

service/ : Logique métier et validation des règles de gestion.

controller/ : Orchestration entre l'interface utilisateur et les services.

config/ : Configuration de la connexion à la base de données.

🛠️ Installation et Lancement

1. Prérequis

Python 3.x

Un serveur MySQL (MAMP local)

Bibliothèque Python : mysql-connector-python

2. Configuration de la base de données

Importez le fichier helpline_db.sql dans votre gestionnaire de base de données (PHPMyAdmin).

3. Installation des dépendances

pip install mysql-connector-python


4. Lancement

python3 main.py


👨‍💻 Auteur

[Franck Ngako] - Apprenti Ingénieur / Master
Projet réalisé dans le cadre de la montée en compétences pour l'alternance.