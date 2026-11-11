
import unittest
import json

from film import Film, favoris_to_json


class TestFilm(unittest.TestCase):

    def setUp(self):
        self.film = Film(
            "Titanic",
            "James Cameron",
            1997,
            9.5
        )

    # Tester la création
    def test_creation(self):
        self.assertEqual(self.film.titre, "Titanic")
        self.assertEqual(self.film.annee, 1997)
        self.assertEqual(self.film.note, 9.5)

    # Tester l'immuabilité
    def test_immutabilite(self):
        with self.assertRaises(AttributeError):
            self.film.note = 8.0

    # Tester la méthode to_json
    def test_to_json(self):
        resultat = json.loads(self.film.to_json())
        self.assertEqual(resultat["titre"], "Titanic")

    # Tester les films classiques
    def test_est_classique(self):
        self.assertTrue(self.film.est_classique())

        film_recent = Film("Avatar", "James Cameron", 2009, 8.5)
        self.assertFalse(film_recent.est_classique())

    # Tester from_json
    def test_from_json(self):
        film = Film.from_json(self.film.to_json())
        self.assertEqual(film, self.film)

    # Tester la comparaison
    def test_comparaison(self):
        film1 = Film("Film A", "Auteur A", 2000, 7.0)
        film2 = Film("Film B", "Auteur B", 2001, 9.0)

        self.assertTrue(film1 < film2)

    # Tester une note invalide
    def test_note_invalide(self):
        with self.assertRaises(ValueError):
            Film("Film", "Auteur", 2000, 11)

    # Tester un titre vide
    def test_titre_vide(self):
        with self.assertRaises(ValueError):
            Film("", "Auteur", 2000, 8.0)

    # Tester une année invalide
    def test_annee_invalide(self):
        with self.assertRaises(ValueError):
            Film("Film", "Auteur", -2000, 8.0)

    # Tester un type invalide
    def test_type_invalide(self):
        with self.assertRaises(TypeError):
            Film("Film", "Auteur", 2000, "excellent")

    # Tester la liste des favoris
    def test_favoris(self):
        favoris = [self.film]
        resultat = json.loads(favoris_to_json(favoris))

        self.assertEqual(len(resultat), 1)
        self.assertEqual(resultat[0]["titre"], "Titanic")


if __name__ == "__main__":
    unittest.main()
