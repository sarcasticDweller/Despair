import easyttuimenus as ttui  # pyright: ignore[reportMissingTypeStubs]
from src.constants import *
import src.playing_cards as playing_cards

def game_loop() -> None:
    PAUSE_TEXT = "Press enter to continue"
    pause = lambda: input(PAUSE_TEXT)
    played_cards = playing_cards.Deck()
    discard = playing_cards.Deck()
    considered_cards = playing_cards.Deck()
    deck = playing_cards.StandardDeck()
    deck.shuffle()
    deck.draw(int(len(deck)*STARTING_DECK_FRACTION)) # starting out with half a deck of cards. ooh, the uncertainty!
    hand = playing_cards.Deck(*deck.draw(HAND_SIZE))

    print("Despair: A Game About Debt")
    pause()
    print("How to Play:\n- Select cards by typing the number left of the colon and press enter\n- Select pairs to play pairs\n- Select sequences of three of the same suit to play straights\n- All other cards will be discarded\n- Press \"0\" when you've selected what you want to play to end your turn\n- When you run out of cards in the deck you get one last turn to play cards\n- All discarded cards and cards left in your hand will weigh against you!")
    pause()
    while len(deck) > 0:
        try:
            hand.extend(deck.draw(HAND_SIZE-len(hand)))
        except:
            hand.extend(deck.empty_deck())
        
        selected = ttui.multiple_choice_menu(f"Despair\n\nStats\nDiscard: {len(discard)}\nPlayed: {len(played_cards)}\nRemaining cards in deck: {len(deck)}\n\nSelect some cards to play", list(hand))
        considered_cards.extend(hand.draw_several_specific(selected))
        contains_pairs, pairs = considered_cards.contains_pairs()
        contains_straights, straights = considered_cards.contains_straights()
        valid = contains_pairs or contains_straights

        if valid:
            played_cards.extend(*pairs, *straights)
            considered_cards.clear()
        else:
            print("I hope you wanted to discard those!")
            discard.extend(considered_cards.empty_deck())
        if contains_pairs:
            print("You played pairs!")
        if contains_straights:
            print("You played straights!")
        pause()

    discard.extend(hand.empty_deck())
    score_discard = len(discard)
    score_played = len(played_cards)
    score = score_played - score_discard
    result_message = "Good job!" if score > 0 else "Better luck next time!"
    print("And that's the game!\nYour remaining cards have been discarded.")
    print(f"Your final score is {score}. {result_message}\nBreakdown:\n- {score_played} played cards\n- Minus {score_discard} discared cards\n- Equals {score} points")
    print("Thanks for playing!")
    pause()
    return


if __name__ == "__main__":
    game_loop()