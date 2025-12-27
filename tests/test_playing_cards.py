import unittest
from src.playing_cards import *
from src.constants import *

class TestCards(unittest.TestCase):

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
        cards = [ # im bad at list slices, so im referencing these bad boys individually
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

        self.deck1 = Deck([
            cards[0],
            cards[1],
            cards[2]
        ])
        self.deck2 = Deck([
            cards[5],
            cards[6],
            cards[7]
        ])
        self.deck3 = Deck([
            cards[8],
            cards[9],
            cards[10]
        ])

    def test_resolves_False_1(self):
        self.assertFalse(self.deck1.contains_straights()[0])

    def test_resolves_False_2(self):
        self.assertFalse(self.deck2.contains_straights()[0])

    def test_resolves_True_1(self):
        contains_straights, _ = self.deck3.contains_straights()
        self.assertTrue(contains_straights)

class TestFindUniqueSequences(unittest.TestCase):

    def test_resolves_True_1(self):
        sequence = [0, 1, 2]
        unique_sequences = find_unique_sequences(sequence, 3)
        self.assertEqual(unique_sequences[0], sequence)

    def test_resolves_True_2(self):
        sequence = [4, 5, 6]
        unique_sequences = find_unique_sequences(sequence, 3)
        self.assertEqual(unique_sequences[0], sequence)

    def test_resolves_True_3(self):
        sequence = [4, 5, 6, 7, 8, 9]
        unique_sequences = find_unique_sequences(sequence, 3)
        print(unique_sequences)
        self.assertEqual(unique_sequences, [[4, 5, 6], [7, 8, 9]])
    
    def test_resolves_Equal_1(self):
        sequence = [2, 3, 4]
        unique_sequence = find_unique_sequences(sequence, 3)
        self.assertEqual(len(unique_sequence), 1)

    def test_resolves_Equal_2(self):
        sequence = [0, 2, 3]
        unique_sequences = find_unique_sequences(sequence, 3)
        print(unique_sequences)
        self.assertEqual(len(unique_sequences), 0)


