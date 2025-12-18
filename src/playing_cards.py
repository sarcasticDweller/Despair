import random, enum

class Suit(enum.Enum):
    SPADE = "spade"
    HEART = "heart"
    CLUB = "club"
    DIAMOND = "diamond"

class Rank(enum.IntEnum):
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

class Card:
    def __init__(self, suit: Suit, rank: Rank) -> None:
        self.suit = suit
        self.rank = rank
    
    def __repr__(self) -> str:
        return f"Card {self.rank.name} of {self.suit.name}"
    
    def __lt__(self, other: "Card") -> bool:
        return self.rank < other.rank
    
    def __gt__(self, other: "Card") -> bool:
        return self.rank > other.rank
    
class Deck:
    def __init__(self, cards: list[Card] = []) -> None:
        self.cards = cards

    def __repr__(self) -> str:
        cards = ""
        for card in self.cards:
            cards += f", {card}"
        return cards
    
    def get_list_of_cards_as_strings(self) -> list[str]:
        card_strings: list[str] = []
        for card in self.cards:
            card_strings.append(f"{card}")
        return card_strings

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self, count: int = 1) -> list[Card]:
        """Will draw `count` cards from the top of the deck and return them as a list of `Card` objects. Will error if there are not enough cards in the deck."""
        drawn_cards, self.cards = self.cards[:count], self.cards[count:]
        return drawn_cards

    def draw_specific_by_index(self, card_index: int) -> Card:
        return self.cards.pop(card_index)
    
    def remove_specific(self, card: Card) -> None:
        self.cards.remove(card)

    def draw_several_specific(self, card_indexes: list[int]) -> list[Card]:
        drawn_cards: list[Card] = []
        for i in card_indexes:
            drawn_cards.append(self.cards[i - 1])
        self.cards = list(set(self.cards).symmetric_difference(drawn_cards)) # removes drawn cards from deck
        return drawn_cards
    
    def empty_deck(self) -> list[Card]:
        cards = self.cards
        self.cards = []
        return cards

    def add(self, card: Card) -> None:
        self.cards.append(card)

    def add_several_to_top_of_deck(self, cards: list[Card]) -> None:
        self.cards = self.cards + cards

    def get_card_data_as_lists(self) -> tuple[list[Suit], list[Rank]]: 
        suits: list[Suit] = []
        ranks: list[Rank] = []
        for card in self.cards:
            suits.append(card.suit)
            ranks.append(card.rank)
        return suits, ranks

    def is_straight(self, length: int = 3) -> bool:
        """Depricated in favor of `contains_straights()`... ?"""
        if len(self.cards) != length:
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
        if len(self.cards) != length:
            return False
        _, ranks = self.get_card_data_as_lists()
        return len(set(ranks)) == 1
    
    def contains_pairs(self, size_of_pair: int = 2) -> tuple[bool, list[list[Card]]]:
        """Checks the deck for pairs of a given length. Supports two-of-a-kind, three-of-a-kind, etc.
        Args:
            size_of_pair (int, optional): The length of the pairs to check for. Defaults to 2 to search for standard pairs.
        Returns:
            tuple[bool, list[list[Card]]]:
                - A boolean indicating whether any pairs of the specified length were found.
                - A list of lists, where each inner list contains `Card` objects representing a pair.
        """
        ranks_dict: dict[int, list[Card]] = {}
        pairs: list[list[Card]] = []
        for card in self.cards:
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

    def contains_straights(self, size_of_straight: int = 3) -> tuple[bool, list[list[Card]]]:
        """Checks the deck for straights of a given length. Supports three-card straights, four-card straights, etc.

        Bug detected! Squash me: ranks ACE, TWO, NINE resolves as a straight when suit is the same

        :param size_of_straight: The length of the straights to check for. Defaults to 3 to search for standard straights.
        :type size_of_straight: int (optional)
        :return: A tuple containing:
            - A boolean indicating whether any straights of the specified length were found.
            - A list of lists, where each inner list contains `Card` objects representing a straight
        :rtype: tuple[bool, list[list[Card]]]
        """

        suits_dict: dict[Suit, list[Card]] = {}
        straights: list[list[Card]] = []

        # group by suit
        for card in self.cards:
            if card.suit not in suits_dict:
                suits_dict[card.suit] = []
            suits_dict[card.suit].append(card) # always add the card to respect larger card decks
        
        for suit in suits_dict:
            suited_cards = sorted(suits_dict[suit])

            # happy case first
            if len(suited_cards) == size_of_straight and suited_cards[-1].rank - suited_cards[0].rank == size_of_straight - 1:
                straights.append(suited_cards)
                continue # to next suit

            # convert cards to list of ints for simpler analysis
            card_ranks = [int(card.rank) for card in suited_cards]
            found_sequences: list[list[int]] = find_unique_sequences(card_ranks, size_of_straight)

            # convert found_sequences back into list[list[card]]
            for sequence in found_sequences:
                straight_cards = [card for rank in sequence for card in suited_cards if card.rank == rank]
                straights.append(straight_cards)


        return len(straights) > 0, straights
    
class StandardDeck(Deck):
    def __init__(self) -> None:
        super().__init__(_standard_deck_generator())

def find_unique_sequences(master_sequence: list[int], sequence_length: int) -> list[list[int]]:
    """Takes a list of integers and returns a two-dimensional list of consecutive sequences of `sequence_length` length found in the list of integers."""
    ms_in_order = sorted(master_sequence)
    working_sequence: list[int] = []
    sequences: list[list[int]] = []
    for i in range(len(master_sequence)):
        if len(working_sequence) == 0:
            working_sequence.append(ms_in_order[i])
            continue
        if ms_in_order[i] - 1 == working_sequence[-1]:
            working_sequence.append(ms_in_order[i])
        if len(working_sequence) == sequence_length:
            sequences.append(working_sequence)
            working_sequence = []

    return sequences

def _standard_deck_generator() -> list[Card]:
    return [Card(s, r) for s in Suit for r in Rank]
