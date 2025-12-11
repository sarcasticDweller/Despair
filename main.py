import easyttuimenus as ttui
import random

suit = ["spade", "heart", "club", "diamond"]
rank = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __repr__(self):
        return f"Card {self.rank} of {self.suit}"
    
    """
    def __eq__(self, other):
        if not isinstance(other, Card):
            raise Exception("Tried to compare a card with not a card")
        return self.rank == other.rank
    """

class Deck:
    def __init__(self, cards):
        self.cards = cards
    def __repr__(self):
        cards = ""
        for card in self.cards:
            cards += f", {card}"
        return cards
    def get_list_of_cards_as_strings(self):
        card_strings = []
        for card in self.cards:
            card_strings.append(f"{card}")
        return card_strings

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, count: int = 1):
        drawn_cards, self.cards = self.cards[:count], self.cards[count:]
        return drawn_cards

    def add(self, card):
        self.cards.append(card)

    def get_card_data_as_lists(self): 
        suits = []
        ranks = []
        for card in self.cards:
            suits.append(card.suit)
            ranks.append(card.rank)
        return suits, ranks

    def is_straight(self, length = 3):
        """
        Docstring for is_straight
        
        :param length: Determines the length of the straight to check for. Typical straights have a length of three.
        :rtype: bool
        """
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
    
    def is_pair(self, length = 2):
        """
        Docstring for is_pair
        
        :param self: Description
        :param length: The amount of cards to check if is pair. Typical pairs are made up of just two cards
        :rtype: bool
        """
        if len(self.cards) != length:
            return False
        _, ranks = self.get_card_data_as_lists()
        return len(set(ranks)) == 1

def standard_deck_generator():
    cards = []
    for s in suit:
        for r in rank:
            cards.append(Card(s, r))
    return cards

def game_loop():
    deck = Deck(standard_deck_generator())
    deck.shuffle()
    deck.draw(len(deck.cards)//2) # starting out with half a deck of cards. ooh, the uncertainty!
    hand = Deck(deck.draw(5)) # standard hand size is 5. maybe variablelize this later
    selected = ttui.multiple_choice_menu("Here is your hand", hand.get_list_of_cards_as_strings())

def main():
    game_loop()

if __name__ == "__main__":
    main()