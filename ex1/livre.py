
from dataclasses import dataclass, asdict, replace
import json


@dataclass(frozen=True, slots=True)
class Livre:
    titre: str
    auteur: str
    annee: int
    prix: float

    # Conversion de l'objet en JSON
    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    # Retourner un nouveau livre avec un prix réduit
    def promo(self, prix_reduit):
        return replace(self, prix=prix_reduit)


# Charger un livre depuis une chaîne JSON
def charger_livre(chaine_json):
    donnees = json.loads(chaine_json)
    return Livre(**donnees)


# Comparer deux livres selon leur prix
def comparer_prix(livre1, livre2):
    return sorted([livre1, livre2], key=lambda livre: livre.prix)


# Programme principal
livre1 = Livre("1984", "George Orwell", 1949, 9.90)
livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943, 12.50)

print("Livre 1 :")
print(livre1.to_json())

print("\nPromotion :")
livre_promo = livre1.promo(7.90)
print(livre_promo.to_json())

print("\nLivre original :")
print(livre1.to_json())

print("\nChargement depuis JSON :")
livre_charge = charger_livre(livre1.to_json())
print(livre_charge)

print("\nComparaison par prix croissant :")
for livre in comparer_prix(livre1, livre2):
    print(livre.titre, "-", livre.prix, "DH")

print("\nÉgalité :", livre1 == livre_charge)
