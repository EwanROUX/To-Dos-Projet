todos = []  # Liste pour stocker les todos

# Fonction pour lister les todos
def lister_todos():
    if not todos:
        print("Aucun todo à afficher.")
    else:
        print("==== Liste des Todos ====")
        for index, todo in enumerate(todos, start=1):
            print(f"{index}. {todo['titre']} (Statut : {todo['statut']})")
        print("=========================")

# Fonction pour créer un todo
def creer_todo():
    titre = input("Entrez le titre du nouveau todo : ")
    todo = {'titre': titre, 'statut': 'À faire'}  # Par défaut, le statut est "À faire"
    todos.append(todo)
    print(f'Todo "{titre}" ajouté avec succès.')

# Fonction pour changer le statut d'un todo
def changer_statut_todo():
    if not todos:
        print("Aucun todo disponible pour changer le statut.")
        return

    lister_todos()
    try:
        index = int(input("Entrez le numéro du todo pour changer son statut : ")) - 1
        if index < 0 or index >= len(todos):
            print("Index invalide.")
            return

        todo = todos[index]
        if todo['statut'] == "À faire":
            todo['statut'] = "Fait"
        elif todo['statut'] == "Fait":
            todo['statut'] = "À faire"  # Correction : statut correctement repassé en "À faire"
        else:
            print(f"Statut inconnu pour le todo : {todo['statut']}")
        print(f"Le statut du todo '{todo['titre']}' est maintenant : {todo['statut']}")
    except ValueError:
        print("Entrée invalide. Veuillez entrer un numéro.")

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
