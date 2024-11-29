# Liste pour stocker les todos
todos = []  # Chaque todo sera représenté comme un dictionnaire avec un titre et un statut.

# Fonction pour lister les todos
def lister_todos():
    if not todos:  # Vérifie si la liste est vide
        print("Aucun todo à afficher.")
    else:
        print("==== Liste des Todos ====")
        for index, todo in enumerate(todos, start=1):
            print(f"{index}. {todo['titre']} - Statut : {todo['statut']}")
        print("=========================")

# Fonction pour créer un todo
def creer_todo():
    titre = input("Entrez le titre du nouveau todo : ")
    todos.append({"titre": titre, "statut": "À faire"})  # Ajoute un todo avec statut par défaut "À faire"
    print(f'Todo "{titre}" ajouté avec succès.')

# Fonction pour changer le statut d'un todo
def changer_statut_todo():
    if not todos:
        print("Aucun todo à modifier.")
        return
    
    lister_todos()
    try:
        choix = int(input("Entrez le numéro du todo à modifier : ")) - 1
        if 0 <= choix < len(todos):  # Vérifie que le choix est valide
            todo = todos[choix]
            if todo["statut"] == "À faire":
                todo["statut"] = "Fait"
            elif todo["statut"] == "Fait":
                todo["statut"] = "À fair"  # Erreur volontaire (sans le 'e')
            print(f'Statut du todo "{todo["titre"]}" mis à jour en : {todo["statut"]}')
        else:
            print("Numéro de todo invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")

# Menu principal
choix = ''
while choix != 'q':
    print("==== Menu Principal ====")
    print("1: Lister les todos")
    print("2: Créer un todo")
    print("3: Changer le statut d'un todo")
    print("q: Quitter")
    choix = input("=> Choix : ")

    if choix == '1':
        lister_todos()
    elif choix == '2':
        creer_todo()
    elif choix == '3':
        changer_statut_todo()
    elif choix == 'q':
        print("Au revoir !")
    else:
        print("Choix invalide, veuillez réessayer.")
