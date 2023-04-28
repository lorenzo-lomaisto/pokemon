class Pokemon:
    def __init__(self, nom, pv=100, niveau=1, attaque=0, defense=0):
        self._nom = nom
        self._pv = pv
        self._niveau = niveau
        self._attaque = attaque
        self._defense = defense

    def afficher_infos(self):
        print(f"Nom: {self._nom}\nPV: {self._pv}\nNiveau: {self._niveau}\nAttaque: {self._attaque}\nDéfense: {self._defense}")