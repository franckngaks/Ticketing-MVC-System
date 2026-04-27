import sys
from controller.employeController import EmployeController
# On importe le contrôleur d'incidents maintenant qu'il est prêt
from controller.incidentController import IncidentController 

def afficher_menu_principal():
    """Affiche les sections disponibles de l'application."""
    print("\n" + "="*50)
    print("      SYSTÈME HELPLINE - INTERFACE DE GESTION")
    print("="*50)
    print("  [1] GESTIONNAIRE D'ANNUAIRE (Employés)")
    print("  [2] GESTIONNAIRE D'INCIDENTS (Tickets)")
    print("  [Q] QUITTER L'APPLICATION")
    print("-" * 50)

def main():
    """
    INITIALISATION ET ROUTAGE PRINCIPAL
    C'est ici que l'application prend vie.
    """
    # 1. Initialisation des contrôleurs (Architecture MVC)
    # Le contrôleur va lui-même instancier le service et le repository
    ctrl_employe = EmployeController()
    ctrl_incident = IncidentController()

    try:
        while True:
            afficher_menu_principal()
            choix = input("👉 Choisissez une section : ").strip().upper()

            if choix == '1':
                # --- SECTION ANNUAIRE ---
                print("\n--- GESTION DES COLLABORATEURS ---")
                print("1. Lister les employés")
                print("2. Ajouter un collaborateur")
                print("3. Modifier un collaborateur")
                print("4. Supprimer un collaborateur")
                print("5. Retour")
                sous_choix = input("Action : ")
                
                if sous_choix == '1':
                    ctrl_employe.afficher_annuaire()
                elif sous_choix == '2':
                    nom = input("Nom : ")
                    prenom = input("Prénom : ")
                    email = input("Email : ")
                    role = input("Rôle (User/Tech/Admin) : ")
                    ctrl_employe.ajouter_collaborateur(nom, prenom, email, role)
                elif sous_choix == '3':
                    id_e = input("ID de l'employé à modifier : ")
                    if id_e.isdigit():
                        nom = input("Nouveau Nom : ")
                        prenom = input("Nouveau Prénom : ")
                        email = input("Nouvel Email : ")
                        role = input("Nouveau Rôle (User/Tech/Admin) : ")
                        pwd = input("Nouveau Mot de passe : ")
                        ctrl_employe.modifier_profil(int(id_e), nom, prenom, email, role, pwd)
                elif sous_choix == '4':
                    id_e = input("ID de l'employé à supprimer : ")
                    if id_e.isdigit():
                        confirm = input(f"❗ Confirmez-vous la suppression de l'employé #{id_e} ? (O/N) : ").upper()
                        if confirm == 'O':
                            ctrl_employe.licencier_employe(int(id_e))
                
            elif choix == '2':
                # --- SECTION INCIDENTS ---
                print("\n--- GESTION DES TICKETS ---")
                print("1. Voir le flux des incidents")
                print("2. Ouvrir un nouveau ticket")
                print("3. Modifier un ticket (Infos/Priorité)")
                print("4. Résoudre un ticket (Tech uniquement)")
                print("5. Retour")
                sous_choix = input("Action : ")

                if sous_choix == '1':
                    ctrl_incident.afficher_liste_incidents()
                elif sous_choix == '2':
                    titre = input("Titre de l'incident : ")
                    prio = input("Priorité (Basse/Moyenne/Haute/Critique) : ")
                    id_u = input("ID de l'employé créateur : ")
                    desc = input("Description complète : ")
                    if id_u.isdigit():
                        ctrl_incident.ouvrir_ticket(titre, prio, int(id_u), desc)
                elif sous_choix == '3':
                    id_t = input("ID du ticket à modifier : ")
                    if id_t.isdigit():
                        titre = input("Nouveau Titre : ")
                        prio = input("Nouvelle Priorité : ")
                        desc = input("Nouvelle Description : ")
                        ctrl_incident.modifier_ticket(int(id_t), titre, prio, desc)
                elif sous_choix == '4':
                    id_t = input("ID du ticket à résoudre : ")
                    id_tech = input("ID du technicien : ")
                    if id_t.isdigit() and id_tech.isdigit():
                        ctrl_incident.resoudre_ticket(int(id_t), int(id_tech))

            elif choix == 'Q':
                print("\n👋 Fermeture sécurisée de l'application. Au revoir !")
                sys.exit()

            else:
                print("⚠️ Option invalide, veuillez recommencer.")

    except KeyboardInterrupt:
        print("\n\n🛑 Interruption détectée. Fermeture du programme.")
        sys.exit()

if __name__ == "__main__":
    main()