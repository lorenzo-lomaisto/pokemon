from PocketMonster import Pokemon

class Normal(Pokemon):
    def __init__(self, nom, pv=100, niveau=1):
        super().__init__(nom, pv, niveau, attaque=10, defense=10)
        self._type = "Normal"
        
class Feu(Pokemon):
    def __init__(self, nom, pv=100, niveau=1):
        super().__init__(nom, pv, niveau, attaque=15, defense=5)
        self._type = "Feu"
        
class Eau(Pokemon):
    def __init__(self, nom, pv=100, niveau=1):
        super().__init__(nom, pv, niveau, attaque=10, defense=15)
        self._type = "Eau"
        
class Terre(Pokemon):
    def __init__(self, nom, pv=100, niveau=1):
        super().__init__(nom, pv, niveau, attaque=5, defense=20)
        self._type = "Terre"