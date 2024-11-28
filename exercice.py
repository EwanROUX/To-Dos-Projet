todos = [] # Liste pour les todos

def lister_todos(): # Fonction pour lister les todos
    if not todos:  # Vérifie si la liste est vide
        print("Aucun todo à afficher.")
    else:
        print("====Liste des Todos====")
        for index, todo in enumerate(todos, start=1):
            print(f"{index}. {todo}")
        print("=========================")

def creer_todo(): # Fonction pour créer un todo
    titre = input("Entrez le titre du nouveau todo : ")
    todos.append(titre)  # Ajoute le todo à la liste
    print(f'Todo "{titre}" ajouté avec succès.')

# Menu principal
choix = ''
while choix != 'q':
    print("==== Menu Principal ====")
    print("1: Lister les todos")
    print("2: Créer un todo")
    print("q: Quitter")
    choix = input("=> Choix : ")

    if choix == '1':
        lister_todos()
    elif choix == '2':
        creer_todo()
    elif choix == 'q':
        print("Au revoir !")
    else:
        print("Choix invalide, veuillez réessayer.")

