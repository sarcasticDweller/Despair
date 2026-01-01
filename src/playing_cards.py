from random import shuffle
from enum import Enum, IntEnum, auto
from typing import List, Dict, Tuple

class Suit(Enum):
    SPADE = "spade"
    HEART = "heart"
    CLUB = "club"
    DIAMOND = "diamond"

class Rank(IntEnum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class SpecialRank(IntEnum):
    ACEHIGH = 14

RankType = Rank | SpecialRank # its hacky, but its the only way i could think to get high-ace support. and i might have to change it later!


class Card:
    """
    Contains a suit and rank enum value that can be used for playing-card games. Supports high and low aces.
    
    :var suit: simple enumerated suit data. Under the hood, it's a `str` (for now).
    :vartype suit: Suit
    :var rank: simple enumerated rank data. Under the hood, it's an `int`.
    :vartype rank: Rank
    """
    def __init__(self, suit: Suit, rank: RankType) -> None:
        self.suit = suit
        self.rank = rank
    
    def __repr__(self) -> str:
        return f"Card {self.rank.name} of {self.suit.name}"
    
    def __lt__(self, other: "Card") -> bool:
        #return self.rank < other.rank
        return True if self.rank == Rank.KING and other.rank == Rank.ACE else self.rank < other.rank
    
    def __gt__(self, other: "Card") -> bool:
        #return self.rank > other.rank
        return True if self.rank == Rank.ACE and other.rank == Rank.KING else self.rank > other.rank
    
class Deck(List[Card]):
    class AcePreference(IntEnum):
        LOW = auto()
        HIGH = auto()
    class AcesMode(IntEnum):
        LOW = auto()
        HIGH = auto()
        BOTH = auto()
    
    _ace_preference: AcePreference = AcePreference.LOW
    _aces_mode: AcesMode = AcesMode.BOTH
    def __init__(self, *cards: Card) -> None:
        super().__init__(cards)
    
    @classmethod
    def set_aces_mode(cls, mode: AcesMode) -> None:
        """
        Determines how aces are played in the game. Possible options are:

        - AcesMode.LOW: Only allow low aces (can be played with a two, but never a King)
        - AcesMode.HIGH: Only allow high aces (can be played with a King, but never a two)
        - AcesMode.BOTH: Allow both high and low aces (can be played with a King or a two)
        """
        cls.aces_mode = mode
    
    @classmethod
    def set_aces_preference(cls, preference: AcePreference) -> None:
        """
        Determines what kind of sequence should be favored when an ace is involved. Possible options are:

        -AcePreference.LOW: When a sequence containing a low ace and a high ace is found, but there's only one ace, favor the lower sequence
        -AcePreference.LOW: When a sequence containing a low ace and a high ace is found, but there's only one ace, favor the higher sequence
        """
        cls.ace_preference = preference

    def shuffle(self) -> None:
        shuffle(self)

    def draw(self, count: int = 1) -> List[Card]:
        """Will draw `count` cards from the top of the deck and return them as a list of `Card` objects. Will error if there are not enough cards in the deck."""
        return [self.pop() for _ in range(count)]

    def draw_several_specific(self, card_indexes: List[int]) -> List[Card]:
        drawn_cards: List[Card] = []
        for i in card_indexes:
            drawn_cards.append(self[i - 1])
        self.cards = list(set(self).symmetric_difference(drawn_cards)) # removes drawn cards from deck
        return drawn_cards
    
    def empty_deck(self) -> List[Card]:
        """Returns the contents of the deck. Designed to easily pipe contents from A to B."""
        old_cards = list(self)
        self.clear()
        return old_cards

    def get_card_data_as_lists(self) -> tuple[List[Suit], List[RankType]]: 
        suits: List[Suit] = []
        ranks: List[RankType] = []
        for card in self:
            suits.append(card.suit)
            ranks.append(card.rank) 
        return suits, ranks
    
    def get_ranks_as_list_of_ints(self, cards: List[Card]) -> List[int]:
        return [int(card.rank) for card in cards]

    def is_straight(self, length: int = 3) -> bool:
        """Depricated in favor of `contains_straights()`... ?"""
        if len(self) != length:
            return False
        suits, ranks = self.get_card_data_as_lists()
        if len(set(suits)) != 1: # eliminate duplicates and count uniques, of which there should only be one
            return False
        ranks = sorted(set(ranks))
        if len(ranks) != length:
            return False
        # for any given length of sequential integers, you can verify that it is sequential if the difference of the last and first items is equal to one less than the length
        return ranks[-1] - ranks[0] == length - 1
    
    def is_pair(self, length: int = 2) -> bool:
        """Depricated in favor of `contains_pairs()`... ?"""
        if len(self) != length:
            return False
        _, ranks = self.get_card_data_as_lists()
        return len(set(ranks)) == 1
    
    def contains_pairs(self, size_of_pair: int = 2) -> Tuple[bool, List[List[Card]]]:
        """Checks the deck for pairs of a given length. Supports two-of-a-kind, three-of-a-kind, etc.

        :param size_of_pair: The length of the pairs to check for. Defaults to 2 to search for standard pairs. I'd like to make this cacheable, but that's a smarter person's job.
        :type size_of_pair: int, (optional)
        :return: A tuple containing:
                - A `bool` indicating whether any pairs of the specified length (`size_of_pair`) were found.
                - A `list` of lists, where each inner `list` contains `Card` objects representing a pair.
        :rtype: Tuple[bool, List[List[Card]]]
        """
        ranks_dict: Dict[int, List[Card]] = {}
        pairs: List[List[Card]] = []
        for card in self:
            if card.rank not in ranks_dict:
                ranks_dict[card.rank] = []
            if card not in ranks_dict[card.rank]:
                ranks_dict[card.rank].append(card)
        for rank in ranks_dict:
            # there may be multiple pairs in the rank
            cards = ranks_dict[rank]

            # worst case first:
            if len(cards) < size_of_pair:
                continue

            # happy case next:
            if len(cards) == size_of_pair: 
                pairs.append(cards)
                continue

            # oh good, there's at least one pair in there

            # neutral case: two+ pairs in the rank
            for i in range(0, len(cards), size_of_pair):
                pair = cards[i:i + size_of_pair]
                pairs.append(pair)

        return len(pairs) > 0, pairs

    def contains_straights(self, size_of_straight: int = 3) -> tuple[bool, List[List[Card]]]:
        """Checks the deck for straights of a given length. Supports three-card straights, four-card straights, etc. Supports high and low aces.

        **IMPORTANT**: If you want to customize how aces work, make sure you `Deck.set_aces_preference` and `Deck.set_aces_mode` before running `Deck.contains_straights`

        **IMPORTANT**: Does NOT support duplicates... yet

        :param size_of_straight: The length of the straights to check for. Defaults to 3 to search for standard straights.
        :type size_of_straight: int (optional)
        :return: A tuple containing:
            - A boolean indicating whether any straights of the specified length were found.
            - A list of lists, where each inner list contains `Card` objects representing a straight
        :rtype: tuple[bool, List[List[Card]]]
        """

        suits_dict: dict[Suit, List[Card]] = {}
        straights: List[List[Card]] = []

        # group by suit
        for card in self:
            suits_dict.setdefault(card.suit, []).append(card)
        for suit in suits_dict:
            suited_cards = sorted(suits_dict[suit])
            if len(suited_cards) < size_of_straight:
                continue

            # happy case 
            if len(suited_cards) == size_of_straight and suited_cards[-1].rank - suited_cards[0].rank == size_of_straight - 1:
                straights.append(suited_cards)
                continue # to next suit

            first_card = suited_cards[0]
            ace_present = first_card.rank == Rank.ACE
            special_card: Card | None = None # it will only be used in scopes where i know it exists, but this is clearer?
            HIGH_ACE = SpecialRank.ACEHIGH

            if ace_present:
                special_card = Card(suit, Rank.ACE)
                special_card.rank = HIGH_ACE # pyright: ignore[reportAttributeAccessIssue] duck-type our way to a high-ace!
                suited_cards.append(special_card)
            
            card_ranks = self.get_ranks_as_list_of_ints(suited_cards)

            found_sequences = [[card for rank in sequence for card in suited_cards if card.rank == rank] for sequence in find_unique_sequences(card_ranks, size_of_straight)]
            if not found_sequences:
                continue

            low_ace_used, high_ace_used = found_sequences[0][0].rank == int(Rank.ACE), found_sequences[-1][-1].rank == HIGH_ACE
            if low_ace_used and high_ace_used:
                if Deck._ace_preference == Deck.AcePreference.LOW:
                    found_sequences.pop(-1)
                if Deck._ace_preference == Deck.AcePreference.HIGH:
                    found_sequences.pop(0)
            elif high_ace_used and not low_ace_used:
                found_sequences[-1][-1] = first_card # which must be an ace, because an ace is present
            
            straights.extend(found_sequences)

        return len(straights) > 0, straights
    
class StandardDeck(Deck):
    def __init__(self) -> None:
        super().__init__(*self._generator())
    
    def _generator(self) -> List[Card]:
        return [Card(s, r) for s in Suit for r in Rank]

def old_find_unique_sequences(master_sequence: List[int], sequence_length: int) -> List[List[int]]:
    """Takes a list of integers and returns a two-dimensional list of consecutive sequences of `sequence_length` length found in the list of integers. Expects the list to be sorted."""
    working_sequence: List[int] = []
    sequences: List[List[int]] = []
    for i in range(len(master_sequence)):
        if len(working_sequence) == 0:
            working_sequence.append(master_sequence[i])
            continue
        if master_sequence[i] - 1 == working_sequence[-1]:
            working_sequence.append(master_sequence[i])
        else:
            working_sequence = [master_sequence[i]]
        if len(working_sequence) == sequence_length:
            sequences.append(working_sequence)
            working_sequence = []

    return sequences

def find_unique_sequences(master_sequence: List[int], sequence_length: int) -> List[List[int]]:
    working_sequences: List[List[int]] =[[]]
    for value in master_sequence:
        next: List[int] = []
        for sequence in working_sequences:
            if len(sequence) == 0 or value - 1 == sequence[-1]: 
                sequence.append(value)
            else:
                next.append(value)
        working_sequences.extend([v] for v in next)
    return [sequence[:sequence_length] for sequence in working_sequences if len(sequence) >= sequence_length]

