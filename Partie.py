import json
import random
from PocketMonster import Pokemon
import Combat
from Afficher import afficher_pokedex 
from Ajouter import ajouter_pokemon

# Import des classes Pokemon et Combat

with open(r"C:\Users\loren\Desktop\git\projet Pokemon\pokemon.json", "r") as f:
    pokemon_data = json.load(f)

with open(r"C:\Users\loren\Desktop\git\projet Pokemon\pokedex.json", "r") as f:
    pokedex_data = json.load(f)

def lancer_partie():
    # Demander au joueur de choisir son Pokémon
    print("Choisissez votre Pokémon :")
    for i, pokemon in enumerate(pokemon_data):
        print(f"{i+1}. {pokemon['nom']} (PV: {pokemon['pv']}, niveau: {pokemon['niveau']})")
    choix_joueur = int(input("Entrez le numéro correspondant à votre choix : "))

    # Créer l'objet Pokemon correspondant au choix du joueur
    pokemon_joueur_data = pokemon_data[choix_joueur-1]
    pokemon_joueur = Pokemon(**pokemon_joueur_data)

    # Choisir un Pokémon adverse de façon aléatoire
    pokemon_adverse_data = random.choice(pokemon_data)
    pokemon_adverse = Pokemon(**pokemon_adverse_data)

    # Créer l'objet Combat et lancer le combat
    combat = Combat(pokemon_joueur, pokemon_adverse)
    vainqueur = combat.lancer_combat()

    # Afficher le résultat du combat
    if vainqueur == pokemon_joueur:
        print(f"Vous avez gagné le combat contre {pokemon_adverse.nom} !")
    else:
        print(f"Vous avez perdu le combat contre {pokemon_adverse.nom}...")

    # Enregistrer le Pokémon rencontré dans le Pokédex
    if pokemon_adverse.nom not in pokedex_data:
        pokedex_data[pokemon_adverse.nom] = pokemon_adverse.to_dict()
        with open("pokedex.json", "w") as f:
            json.dump(pokedex_data, f, indent=4)

    # Afficher le contenu du Pokédex
    afficher_pokedex()

    # boucle principale du menu
while True:
    print("Que voulez-vous faire ?")
    print("1. Lancer une partie")
    print("2. Ajouter un nouveau Pokémon")
    print("3. Afficher le Pokédex")
    print("4. Quitter")
    choix = input("Entrez le numéro de votre choix : ")

    if choix == "1":
        lancer_partie()
    elif choix == "2":
        ajouter_pokemon()
    elif choix == "3":
        afficher_pokedex()
    elif choix == "4":
        break
    else:
        print("Choix invalide. Veuillez entrer un numéro entre 1 et 4.")