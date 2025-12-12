import easyttuimenus as ttui  # pyright: ignore[reportMissingTypeStubs]
import random

suit = ["spade", "heart", "club", "diamond"]
rank = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

class Card:
    def __init__(self, suit: str, rank: int) -> None:
        self.suit = suit
        self.rank = rank
    
    def __repr__(self) -> str:
        return f"Card {self.rank} of {self.suit}"

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

    def add(self, card: Card) -> None:
        self.cards.append(card)

    def get_card_data_as_lists(self) -> tuple[list[str], list[int]]: 
        suits: list[str] = []
        ranks: list[int] = []
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
        if len(self.cards) != length:
            return False
        _, ranks = self.get_card_data_as_lists()
        return len(set(ranks)) == 1

def standard_deck_generator() -> list[Card]:
    cards: list[Card] = []
    for s in suit:
        for r in rank:
            cards.append(Card(s, r))
    return cards

def game_loop() -> None:
    deck = Deck(standard_deck_generator())
    deck.shuffle()
    deck.draw(len(deck.cards)//2) # starting out with half a deck of cards. ooh, the uncertainty!
    hand = Deck(deck.draw(5)) # standard hand size is 5. maybe variablelize this later
    selected = ttui.multiple_choice_menu("Here is your hand", hand.get_list_of_cards_as_strings())
    considered_cards = Deck(hand.draw_several_specific(selected))
    if len(considered_cards.cards) == 2:
        print(considered_cards.is_pair())
    if len(considered_cards.cards) == 3:
        print(considered_cards.is_straight())
    else:
        print("i hope you wanted to toss those!")


         

def main() -> None:
    game_loop()

if __name__ == "__main__":
    main()