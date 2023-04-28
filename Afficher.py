import json

def afficher_pokedex():
    with open("pokedex.json", "r") as f:
        pokedex = json.load(f)
    print("Pokédex :")
    for pokemon in pokedex.values():
        print("Nom :", pokemon["nom"])
        print("PV :", pokemon["pv"])
        print("Niveau :", pokemon["niveau"])
        print("Attaque :", pokemon["attaque"])
        print("Défense :", pokemon["defense"])
        print("Type :", pokemon["type"])
        print("-------------")