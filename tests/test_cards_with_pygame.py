import unittest, sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets")))
import cards_with_graphics
import playing_cards

class TestCardsWithGraphics(unittest.TestCase):
    def test_working(self):
        print("All working")
        self.assertEqual(0, 0)
    def test_card_sprite(self):
        card = cards_with_graphics.CardSprite(
            playing_cards.Card(
                playing_cards.Suit.HEART, 
                playing_cards.Rank.ACE
                ))
        self.assertEqual(card.card_data.rank, playing_cards.Rank.ACE)