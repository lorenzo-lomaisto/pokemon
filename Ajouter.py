import json

def ajouter_pokemon(nom, pv, attaque, defense):
    with open('pokemon.json', 'r') as f:
        data = json.load(f)
    
    # Vérifier si le Pokémon n'existe pas déjà
    for pokemon in data['pokemon']:
        if pokemon['nom'] == nom:
            print(f"Le Pokémon {nom} existe déjà dans le fichier.")
            return
    
    # Ajouter les informations du nouveau Pokémon à la variable data
    data['pokemon'].append({
        'nom': nom,
        'pv': pv,
        'attaque': attaque,
        'defense': defense
    })
    
    # Écrire la variable data dans le fichier au format JSON
    with open('pokemon.json', 'w') as f:
        json.dump(data, f, indent=4)
        
    print(f"Le Pokémon {nom} a été ajouté au fichier.")