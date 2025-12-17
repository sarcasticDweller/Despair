import unittest, sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets")))
import cards_with_graphics
import playing_cards

STOCK_CARD = cards_with_graphics.CardSprite(
    playing_cards.Card(
        playing_cards.Suit.HEART,
        playing_cards.Rank.ACE
    )
)

class TestCardsWithGraphics(unittest.TestCase):
    def test_working(self):
        # if it errors, it aint working!
        print("Hello world")

    def test_CardSprite_initialization(self):
        card = STOCK_CARD
        self.assertIsInstance(card, cards_with_graphics.CardSprite)
    
    def test_CardSprite_rects(self):
        card = STOCK_CARD
        print(card.card_image)