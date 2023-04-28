import random
import json

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
    
    def est_en_vie(self, pokemon):
        """Vérifie si un Pokémon est en vie"""
        return pokemon.pv > 0
    
    def nom_vainqueur(self):
        """Renvoie le nom du vainqueur"""
        if not self.est_en_vie(self.pokemon1):
            return self.pokemon2.nom
        elif not self.est_en_vie(self.pokemon2):
            return self.pokemon1.nom
        else:
            return None
    
    def peut_attaquer(self):
        """Détermine si un Pokémon peut attaquer"""
        return random.randint(0, 1) == 1
    
    def calcule_degats(self, attaquant, defenseur):
        """Calcule les dégâts infligés par une attaque"""
        efficacite = attaquant.type.multiplie_attaque(defenseur.type)
        degats = int(attaquant.attaque * efficacite - defenseur.defense)
        return max(0, degats)  # Les dégâts ne peuvent pas être négatifs
    
    def reduit_pvs(self, pokemon, degats):
        """Réduit les points de vie d'un Pokémon en fonction de sa défense"""
        pokemon.pv -= max(0, degats - pokemon.defense)
    
    def nom_perdant(self):
        """Renvoie le nom du Pokémon perdant"""
        if not self.est_en_vie(self.pokemon1):
            return self.pokemon1.nom
        elif not self.est_en_vie(self.pokemon2):
            return self.pokemon2.nom
        else:
            return None
    
    def enregistre_pokemon(self, pokemon):
        """Enregistre le Pokémon rencontré dans le Pokédex"""
        try:
            with open('pokedex.json', 'r') as f:
                pokedex = json.load(f)
        except FileNotFoundError:
            pokedex = {}
        if pokemon.nom in pokedex:
            print("Ce Pokémon a déjà été enregistré dans le Pokédex !")
        else:
            pokedex[pokemon.nom] = {
                'type': pokemon.type.nom,
                'pv': pokemon.pv,
                'attaque': pokemon.attaque,
                'defense': pokemon.defense
            }
            with open('pokedex.json', 'w') as f:
                json.dump(pokedex, f)