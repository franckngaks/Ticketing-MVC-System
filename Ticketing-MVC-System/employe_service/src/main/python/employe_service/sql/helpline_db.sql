-- ==========================================================
-- SCRIPT DE CRÉATION DE LA BASE DE DONNÉES HELPLINE
-- À exécuter dans PHPMyAdmin
-- ==========================================================

-- 1. Création de la base de données (si elle n'existe pas)
CREATE DATABASE IF NOT EXISTS helpline_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE helpline_db;

-- 2. Création de la table des Employés (Service Identity)
CREATE TABLE IF NOT EXISTS employes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('User', 'Tech', 'Admin') DEFAULT 'User',
    date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- 3. Insertion de quelques données de test pour vérifier le fonctionnement
INSERT INTO employes (nom, prenom, email, password_hash, role) VALUES 
('Durand', 'Jean', 'jean.durand@helpline.fr', 'hash_secu_123', 'Tech'),
('Lefebvre', 'Marie', 'marie.le@client.fr', 'hash_secu_456', 'User');

