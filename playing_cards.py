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
        return f"Card {self.rank} of {self.suit}"
    
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
    
    def make_standard_deck(self) -> None:
        """Creates a standard deck of 52 playing cards. Should later be outmoded for a subclass."""
        self.cards = _standard_deck_generator()

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

    def draw_specific(self, card_index: int) -> Card:
        return self.cards.pop(card_index)

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
            if len(ranks_dict[rank]) == size_of_pair: #strictly enforce length of pairs
                pairs.append(ranks_dict[rank])
        return (len(pairs) > 0, pairs)

    def contains_straights(self, size_of_straight: int = 3) -> tuple[bool, list[list[Card]]]:
        """Checks the deck for straights of a given length. Supports three-card straights, four-card straights, etc.
        Args:
            size_of_straight (int, optional): The length of the straights to check for. Defaults to 3 to search for standard straights.
        Returns:
            tuple[bool, list[list[Card]]]:
                - A boolean indicating whether any straights of the specified length were found.
                - A list of lists, where each inner list contains `Card` objects representing a straight.
        """
        suits_dict: dict[Suit, list[Card]] = {}
        straights: list[list[Card]] = []
        for card in self.cards:
            if card.suit not in suits_dict:
                suits_dict[card.suit] = []
            if card not in suits_dict[card.suit]:
                suits_dict[card.suit].append(card)
        
        for suit in suits_dict:
            suited_cards = sorted(suits_dict[suit])

            # happy case: suited_cards contains only cards in the straight
            # neutral case: suited_cards contains a straight *somewhere*
            # annoyed case: suited_cards contains *multiple* straights
            # sad case: no straight at all :(

            # happy case first
            if len(suited_cards) == size_of_straight and suited_cards[-1].rank - suited_cards[0].rank == size_of_straight - 1:
                straights.append(suited_cards)
                continue

            # neutral and annoyed cases
            rank_values = [int(card.rank) for card in suited_cards]
            found_sequences = _find_sequences(rank_values, size_of_straight)
            for sequence in found_sequences:
                straight_cards: list[Card] = []
                for rank in sequence:
                    for card in suited_cards:
                        if card.rank == rank:
                            straight_cards.append(card)
                            break
                straights.append(straight_cards)

        return len(straights) > 0, straights


def _find_sequences(master_list: list[int], length_of_sequence: int) -> list[list[int]]:
    # vibe coding time. im sorry dad
    sequences: list[list[int]] = []
    length = len(master_list)

    for i in range(length):
        current_sequence = [master_list[i]]
        
        # Check for the next length_of_sequence-1 integers to form a sequence
        for j in range(1, length_of_sequence):
            next_value = master_list[i] + j
            if next_value in master_list:
                current_sequence.append(next_value)
            else:
                break

        # If we found a full sequence of length length_of_sequence, add it to results
        if len(current_sequence) == length_of_sequence:
            sequences.append(current_sequence)

    return sequences


def _standard_deck_generator() -> list[Card]:
    cards: list[Card] = []
    for s in Suit:
        for r in Rank:
            cards.append(Card(s, r))
    return cards

if __name__ == "__main__":
    deck = Deck()
    deck.make_standard_deck()
    deck.shuffle()
    hand = Deck(deck.draw(25))
    print(hand)
    print(hand.contains_pairs())
    print(hand.contains_straights())