# Test for Scissor Paper Rock game using Test Driven Development

import unittest
from unittest import mock
from rockPaperScissor import RockPaperScissor


class GameTestCase(unittest.TestCase):
    game = RockPaperScissor()

    def test_computerChoice(self):
        self.assertIn(self.game.computerChoice(), ["r", "p", "s"], msg="Invalid option chosen by computer.") # Testing if computer choose these options

    def test_playerChoice(self):
        with mock.patch('builtins.input', return_value="p"):
            assert self.game.PlayerChoice() in ["r", "p", "s", "q", "rs"]  # testing player's input


    def test_pointAdd(self):
        self.assertEqual(3, self.game.pointAdd(2), msg="Incorrect point addition.")  # testing point adition to winner of a round

    def test_winningPoint(self):
        self.assertFalse(self.game.winningPoint(4))
        self.assertTrue(self.game.winningPoint(5))   # Testing if either computer or player gets 5 points to win the game


    def test_setWinner(self):
         #Testing of compaison and tsting of determination of winner

        self.assertEqual("tie", self.game.setWinner("r", "r"), msg="Invalid winner")  
        self.assertEqual("computer", self.game.setWinner("r", "p"), msg="Invalid winner") 
        self.assertEqual("player", self.game.setWinner("r", "s"), msg="Invalid winner")  
        self.assertEqual("player", self.game.setWinner("p", "r"), msg="Invalid winner")  
        self.assertEqual("tie", self.game.setWinner("p", "p"), msg="Invalid winner")  
        self.assertEqual("computer", self.game.setWinner("p", "s"), msg="Invalid winner")  
        self.assertEqual("computer", self.game.setWinner("s", "r"), msg="Invalid winner")  
        self.assertEqual("player", self.game.setWinner("s", "p"), msg="Invalid winner")  
        self.assertEqual("tie", self.game.setWinner("s", "s"), msg="Invalid winner")  



if __name__ == '__main__':
    unittest.main()
