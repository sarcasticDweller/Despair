import unittest
from src.playing_cards import *
from src.constants import *

class TestCardsSupportHighAndLowAces(unittest.TestCase):

    def setUp(self):
        self.ace = Card(Suit.HEART, Rank.ACE)
        self.king = Card(Suit.SPADE, Rank.KING)
        self.num_card = Card(Suit.CLUB, Rank.FOUR)
    
    def test_ace_beats_king(self):
        self.assertTrue(self.ace > self.king)
    
    def test_king_loses_to_ace(self):
        self.assertTrue(self.king < self.ace)
    
    def test_king_beats_num(self):
        self.assertTrue(self.king > self.num_card)
    
    def test_num_loses_to_king(self):
        self.assertTrue(self.num_card < self.king)
    
    def test_num_beats_ace(self):
        self.assertTrue(self.num_card > self.ace)
    
    def test_ace_loses_to_num(self):
        self.assertTrue(self.ace < self.num_card)

class TestDeckContainsStraights(unittest.TestCase):

    def setUp(self):
        self.cards = [ # im bad at list slices, so im referencing these bad boys individually
            Card(Suit.HEART, Rank.ACE),    # 0
            Card(Suit.HEART, Rank.TWO),    # 1
            Card(Suit.HEART, Rank.NINE),   # 2
            Card(Suit.HEART, Rank.TEN),    # 3
            Card(Suit.HEART, Rank.QUEEN),  # 4
            Card(Suit.HEART, Rank.FOUR),   # 5
            Card(Suit.CLUB, Rank.ACE),     # 6
            Card(Suit.DIAMOND, Rank.ACE),  # 7
            Card(Suit.SPADE, Rank.TWO),    # 8
            Card(Suit.SPADE, Rank.THREE),  # 9
            Card(Suit.SPADE, Rank.FOUR)    # 10
        ]

        self.deck1 = Deck(
            self.cards[0],
            self.cards[1],
            self.cards[2]
        )
        self.deck2 = Deck(
            self.cards[5],
            self.cards[6],
            self.cards[7]
        )
        self.deck3 = Deck(
            self.cards[8],
            self.cards[9],
            self.cards[10]
        )

    def test_deck_with_hearts_ace_two_three_ThusTrue(self):
        deck = Deck(
            Card(Suit.HEART, Rank.ACE),
            Card(Suit.HEART, Rank.TWO),
            Card(Suit.HEART, Rank.THREE)
        )
        self.assertTrue(deck.contains_straights()[0])

    def test_deck_with_hearts_queen_king_ace_ThusTrue(self):
        deck = Deck(
            Card(Suit.HEART, Rank.QUEEN),
            Card(Suit.HEART, Rank.KING),
            Card(Suit.HEART, Rank.ACE)
        )
        self.assertTrue(deck.contains_straights()[0])
    
    def test_deck_too_small_for_sequence_ThusFalse(self):
        deck = Deck(Card(Suit.HEART, Rank.ACE))
        self.assertFalse(deck.contains_straights()[0])
    
    def test_deck_hearts_nonsequential_values_ThusFalse(self):
        deck = Deck(
            Card(Suit.HEART, Rank.ACE),
            Card(Suit.HEART, Rank.THREE),
            Card(Suit.HEART, Rank.SEVEN),
        )
        self.assertFalse(deck.contains_straights()[0])
    
    def test_deck_with_mixed_suits_ace_two_three_ThusFalse(self):
        deck = Deck(
            Card(Suit.CLUB, Rank.ACE),
            Card(Suit.DIAMOND, Rank.TWO),
            Card(Suit.HEART, Rank.THREE)
        )
        self.assertFalse(deck.contains_straights()[0])
    
    def test_deck_with_duplicate_and_sequence_of_number_cards_ThusTrue(self):
        deck = Deck(
            Card(Suit.HEART, Rank.TWO),
            Card(Suit.HEART, Rank.TWO),
            Card(Suit.HEART, Rank.THREE),
            Card(Suit.HEART, Rank.THREE),
            Card(Suit.HEART, Rank.FOUR),
            Card(Suit.HEART, Rank.FOUR),
        )
        self.assertTrue(deck.contains_straights()[0])

class TestUniqueSequences(unittest.TestCase):
    def test_new_1_2_3_len3_ThusTrue(self):
        sequence, length = [1, 2, 3], 3
        expected = [[1, 2, 3]]
        actual = find_unique_sequences(sequence, length)
        self.assertEqual(expected, actual)
    
    def test_new_12_13_14_len3_ThusTrue(self):
        sequence, length = [12, 13, 14], 3 
        expected = [sequence]
        actual = find_unique_sequences(sequence, length)
        self.assertEqual(expected, actual)
