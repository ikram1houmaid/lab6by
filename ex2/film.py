
from dataclasses import dataclass, asdict
import json


@dataclass(frozen=True, slots=True)
class Film:
    titre: str
    realisateur: str
    annee: int
    note: float

    def __post_init__(self):
        if not isinstance(self.titre, str) or not self.titre.strip():
            raise ValueError("Le titre doit être une chaîne non vide.")

        if not isinstance(self.realisateur, str) or not self.realisateur.strip():
            raise ValueError("Le réalisateur doit être une chaîne non vide.")

        if type(self.annee) is not int or self.annee <= 0:
            raise ValueError("L'année doit être un entier positif.")

        if isinstance(self.note, bool) or not isinstance(self.note, (int, float)):
            raise TypeError("La note doit être un nombre.")

        if not 0 <= self.note <= 10:
            raise ValueError("La note doit être comprise entre 0 et 10.")

    # Conversion en JSON
    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    # Vérifier si le film est classique
    def est_classique(self):
        return self.annee < 2000

    # Chargement depuis JSON
    @classmethod
    def from_json(cls, chaine_json):
        donnees = json.loads(chaine_json)
        return cls(**donnees)

    # Comparaison naturelle selon la note
    def __lt__(self, autre):
        if not isinstance(autre, Film):
            return NotImplemented
        return self.note < autre.note


# Sérialisation de plusieurs films
def favoris_to_json(favoris):
    return json.dumps(
        [asdict(film) for film in favoris],
        ensure_ascii=False
    )


# Programme principal
if __name__ == "__main__":

    film1 = Film("Titanic", "James Cameron", 1997, 9.5)
    film2 = Film("Avatar", "James Cameron", 2009, 8.5)
    film3 = Film("Inception", "Christopher Nolan", 2010, 9.0)

    print("Film en JSON :")
    print(film1.to_json())

    print("\nFilm classique :")
    print(film1.est_classique())

    print("\nChargement depuis JSON :")
    film_charge = Film.from_json(film1.to_json())
    print(film_charge)

    print("\nFilms triés par note croissante :")
    films = sorted([film1, film2, film3])

    for film in films:
        print(film.titre, "-", film.note)

    print("\nListe des favoris en JSON :")
    favoris = [film1, film2, film3]
    print(favoris_to_json(favoris))
