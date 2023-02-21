import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("card1", 1)
        self.card2 = Card("card2", 3)
        self.card3 = Card("card6", 6)
        self.card_game = CardGame()
        self.cards = [self.card1, self.card2, self.card3]


    def testCheckForAce(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card1))
        
    
    def testHighestCard(self):
        self.assertEqual(self.card2, self.card_game.highest_card(self.card1, self.card2))

    def testCardTotal(self):
        self.assertEqual("You have a total of 10", self.card_game.cards_total(self.cards))
