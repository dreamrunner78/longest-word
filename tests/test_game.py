import unittest
import string
from game import Game

class TestGame(unittest.TestCase):

    def test_game_initialization(self):
        game = Game()
        grid = game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_game_wordvalidationOK(self):
        game = Game()
        game.grid=['H','E','L','O','H','E','L','O','R']
        self.assertEqual(game.is_valid("hello"), True)

    def test_game_wordvalidationKO(self):
        game = Game()
        game.grid=['H','E','L','O','H','E','L','O','R']
        self.assertEqual(game.is_valid("TEST"), False)


    def test_unknown_word_is_invalid(self):
      new_game = Game()
      new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
      self.assertIs(new_game.is_valid('FEUN'), False)

