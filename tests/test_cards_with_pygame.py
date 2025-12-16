#import cards_with_graphics as cwp
import playing_cards as pc
import unittest

class TestCardSpriteInitialization(unittest.TestCase):
    def test_unit_tests_work(self):
        card = pc.Card(pc.Suit.HEART, pc.Rank.ACE)
        self.assertEqual(card.suit, pc.Suit.HEART)
    def test_card_sprite_creation(self):
        card_data = pc.Card(pc.Suit.HEART, pc.Rank.ACE)
        card = cwp.CardSprite(card_data, facing_up=False)
        self.assertEqual(card.card_rect.width, 32)

