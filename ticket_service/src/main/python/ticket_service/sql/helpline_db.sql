-- ==========================================================
-- SCRIPT DE CRÉATION DE LA BASE DE DONNÉES HELPLINE
-- À exécuter dans PHPMyAdmin
-- ==========================================================

-- 1. Création de la base de données (si elle n'existe pas)
CREATE DATABASE IF NOT EXISTS helpline_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE helpline_db;

-- 2. Création de la table des Incidents (Service Ticketing)
CREATE TABLE IF NOT EXISTS incidents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titre VARCHAR(150) NOT NULL,
    priorite ENUM('Basse', 'Moyenne', 'Haute', 'Critique') DEFAULT 'Basse',
    statut ENUM('Ouvert', 'En cours', 'Résolu') DEFAULT 'Ouvert',
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_createur INT NOT NULL,
    id_technicien INT NULL,
    description TEXT,
    -- Définition des relations (Clés Étrangères)
    CONSTRAINT fk_createur FOREIGN KEY (id_createur) REFERENCES employes(id) ON DELETE CASCADE,
    CONSTRAINT fk_technicien FOREIGN KEY (id_technicien) REFERENCES employes(id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- 3. Insertion de quelques données de test pour vérifier le fonctionnement
INSERT INTO incidents (titre, priorite, id_createur) VALUES 
('Panne réseau étage 3', 'Haute', 2),
('Problème accès VPN', 'Moyenne', 2);