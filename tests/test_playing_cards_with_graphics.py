import unittest, sys, os, pygame
# is this all even necessary?
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets")))
import src.cards_with_graphics as cards_with_graphics
import src.playing_cards as playing_cards # pyright: ignore[reportUnusedImport]
from src.constants import *

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

sprite = cards_with_graphics.CardSprite(STOCK_CARD, (0, 0))

class TestCardsWithGraphics(unittest.TestCase):
    def test_working(self):
        # if it errors, it aint working!
        print("Hello world")

    def test_CardSprite_initialization(self):
        card = sprite
        self.assertIsInstance(card, cards_with_graphics.CardSprite)
    
