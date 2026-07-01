useCaseDiagram
    actor "Utilisateur" as U
    actor "Technicien" as T
    actor "Administrateur" as A

    package "Système de Gestion Helpline" {
        usecase "Créer un ticket d'incident" as UC1
        usecase "Consulter la liste des tickets" as UC2
        usecase "Modifier un ticket" as UC3
        usecase "Résoudre un incident" as UC4
        usecase "Gérer l'annuaire (CRUD Employés)" as UC5
    }

    U --> UC1
    U --> UC2
    T --> UC2
    T --> UC3
    T --> UC4
    A --> UC5
    A --> UC2


classDiagram
    class IncidentController {
        -service: IncidentService
        +afficher_liste_incidents()
        +ouvrir_ticket(titre, prio, desc)
        +modifier_ticket(id, titre, prio, desc)
    }

    class IncidentService {
        -repository: IncidentRepository
        +lister_incidents()
        +ouvrir_ticket(titre, prio, user_id, desc)
        +modifier_ticket(id, titre, prio, desc)
        +cloturer_incident(id, tech_id)
    }

    class IncidentRepository {
        +find_all()
        +save(titre, prio, user_id, desc)
        +update(id, titre, prio, desc)
        +update_status_to_resolved(id, tech_id)
    }

    class Incident {
        +int id
        +string titre
        +string priorite
        +string statut
        +string description
    }

    IncidentController ..> IncidentService : utilise
    IncidentService ..> IncidentRepository : utilise
    IncidentRepository ..> Incident : manipule


stateDiagram-v2
    [*] --> Ouvert : Signalement par l'employé
    Ouvert --> EnCours : Assignation à un technicien
    EnCours --> Résolu : Intervention terminée
    Résolu --> [*] : Archivage
    
    state EnCours {
        [*] --> Diagnostic
        Diagnostic --> Réparation
    }