import unittest
from animals import *


class TestAnimalKingdom(unittest.TestCase):
    def setUp(self):
        self.animal = Animal("Animal1", 1985)
        self.mammal = Mammal("Panda", 1869)
        self.bird = Bird("Pigeon", 1837)
        self.fish = Fish("Pigeon", 1837)

    def test_animal(self):

        self.assertTrue(isinstance(self.animal, Animal))

        expected_name = "Animal1"
        actual_name = self.animal.name
        self.assertEqual(expected_name, actual_name)

        expected_year_discovered = 1985
        actual_year_discovered = self.animal.year_discovered
        self.assertEqual(expected_year_discovered, actual_year_discovered)

    def test_mammals(self):

        self.assertTrue(isinstance(self.mammal, Mammal))
        self.assertTrue(isinstance(self.mammal, Animal))

        expected_move = "walk"
        actual_move = self.mammal.move()
        self.assertEqual(expected_move, actual_move)

        expected_breath = "lungs"
        actual_breath = self.mammal.breath()
        self.assertEqual(expected_breath, actual_breath)

        expected_reproduce = "live births"
        actual_reproduce = self.mammal.reproduce()
        self.assertEqual(expected_reproduce, actual_reproduce)

    def test_birds(self):

        self.assertTrue(isinstance(self.bird, Bird))
        self.assertTrue(isinstance(self.bird, Animal))

        expected_move = "fly"
        actual_move = self.brid.move()
        self.assertEqual(expected_move, actual_move)

        expected_breath = "lungs"
        actual_breath = self.brid.breath()
        self.assertEqual(expected_breath, actual_breath)

        expected_reproduce = "eggs"
        actual_reproduce = self.brid.reproduce()
        self.assertEqual(expected_reproduce, actual_reproduce)

    def test_fish(self):

        self.assertTrue(isinstance(self.fish, Fish))
        self.assertTrue(isinstance(self.fish, Animal))

        expected_move = "swim"
        actual_move = self.fish.move()
        self.assertEqual(expected_move, actual_move)

        expected_breath = "gills"
        actual_breath = self.fish.breath()
        self.assertEqual(expected_breath, actual_breath)

        expected_reproduce = "eggs"
        actual_reproduce = self.fish.reproduce()
        self.assertEqual(expected_reproduce, actual_reproduce)


if __name__ == "__main__":
    unittest.main()
