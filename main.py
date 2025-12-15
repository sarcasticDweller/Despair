import easyttuimenus as ttui  # pyright: ignore[reportMissingTypeStubs]
import playing_cards # pyright: ignore[reportMissingTypeStubs]
from constants import *

def text_game_loop() -> None:
    PAUSE_TEXT = "Press enter to continue"
    pause = lambda: input(PAUSE_TEXT)
    played_cards = playing_cards.Deck()
    discard = playing_cards.Deck()
    considered_cards = playing_cards.Deck()
    deck = playing_cards.Deck(playing_cards.standard_deck_generator())
    deck.shuffle()
    deck.draw(int(len(deck.cards)*STARTING_DECK_FRACTION)) # starting out with half a deck of cards. ooh, the uncertainty!
    hand = playing_cards.Deck(deck.draw(HAND_SIZE))

    print("Despair: A Game About Debt")
    pause()
    print("How to Play:\n- Select cards by typing the number left of the colon and press enter\n- Select pairs to play pairs\n- Select sequences of three of the same suit to play straights\n- All other cards will be discarded\n- Press \"0\" when you've selected what you want to play to end your turn\n- When you run out of cards in the deck you get one last turn to play cards\n- All discarded cards and cards left in your hand will weigh against you!")
    pause()
    while len(deck.cards) > 0:
        try:
            hand.add_several_to_top_of_deck(deck.draw(HAND_SIZE-len(hand.cards)))
        except:
            hand.add_several_to_top_of_deck(deck.empty_deck())
        
        selected = ttui.multiple_choice_menu(f"Despair\n\nStats\nDiscard: {len(discard.cards)}\nPlayed: {len(played_cards.cards)}\nRemaining cards in deck: {len(deck.cards)}\n\nSelect some cards to play", hand.get_list_of_cards_as_strings())
        considered_cards.add_several_to_top_of_deck(hand.draw_several_specific(selected))
        


def game_loop() -> None:
    PAUSE_TEXT = "Press enter to continue"
    played_cards = playing_cards.Deck()
    discard = playing_cards.Deck()
    considered_cards = playing_cards.Deck()
    deck = playing_cards.Deck(playing_cards.standard_deck_generator())
    deck.shuffle()
    deck.draw(len(deck.cards)//2) # starting out with half a deck of cards. ooh, the uncertainty!
    hand = playing_cards.Deck(deck.draw(HAND_SIZE)) 

    print("Despair: A Game About Debt")
    input(PAUSE_TEXT)
    print("How to Play:\n- Select cards by typing the number left of the colon and press enter\n- Select pairs to play pairs\n- Select sequences of three of the same suit to play straights\n- All other cards will be discarded\n- Press \"0\" when you've selected what you want to play to end your turn\n- When you run out of cards in the deck you get one last turn to play cards\n- All discarded cards and cards left in your hand will weigh against you!")
    input(PAUSE_TEXT)

    
    while len(deck.cards) > 0:
        try: # trying to decide how i want to handle errors on Deck.draw()
            hand.add_several_to_top_of_deck(deck.draw(HAND_SIZE-len(hand.cards)))
        except:
            hand.add_several_to_top_of_deck(deck.empty_deck())
        selected = ttui.multiple_choice_menu(f"Despair\n\nStats\nDiscard: {len(discard.cards)}\nPlayed: {len(played_cards.cards)}\nRemaining cards in deck: {len(deck.cards)}\n\nSelect some cards to play", hand.get_list_of_cards_as_strings())
        considered_cards.add_several_to_top_of_deck(hand.draw_several_specific(selected))
        if len(considered_cards.cards) == 2:
            is_pair = considered_cards.is_pair()
            print("checking if pair")
            if is_pair:
                print("That's a valid pair!")
                played_cards.add_several_to_top_of_deck(considered_cards.empty_deck())
            else:
                print("i hope you wanted to toss those!")
                discard.add_several_to_top_of_deck(considered_cards.empty_deck())
        elif len(considered_cards.cards) == 3:
            print("checking if straight")
            is_straight = considered_cards.is_straight()
            if is_straight:
                print("That's a valid straight!")
                played_cards.add_several_to_top_of_deck(considered_cards.empty_deck())
            else:
                print("i hope you wanted to toss those!")
                discard.add_several_to_top_of_deck(considered_cards.empty_deck())
        else:
            print("i hope you wanted to toss those!")
            discard.add_several_to_top_of_deck(considered_cards.empty_deck())
        input(PAUSE_TEXT)
    discard.add_several_to_top_of_deck(hand.empty_deck())
    print("And that's the game!\nYour remaining cards have been discarded.")
    score_discard = len(discard.cards)
    score_played = len(played_cards.cards)
    score = score_played - score_discard
    print(f"Your final score is {score}.\nBreakdown:\n- {score_played} played cards minus {score_discard} discared cards equals {score}")
    print("Thanks for playing!")
    input(PAUSE_TEXT)


         

def main() -> None:
    game_loop()

if __name__ == "__main__":
    main()