import easyttuimenus as ttui  # pyright: ignore[reportMissingTypeStubs]
from constants import *
import pygame, argparse, playing_cards # pyright: ignore[reportMissingTypeStubs]

def graphics_game_loop() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_CAPTION)
    clock = pygame.time.Clock()
    dt = 0
    fps = FPS
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

def text_game_loop() -> None:
    PAUSE_TEXT = "Press enter to continue"
    pause = lambda: input(PAUSE_TEXT)
    played_cards = playing_cards.Deck()
    discard = playing_cards.Deck()
    considered_cards = playing_cards.Deck()
    deck = playing_cards.StandardDeck()
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
        contains_pairs, pairs = considered_cards.contains_pairs()
        contains_straights, straights = considered_cards.contains_straights()
        
        def validate_and_remove(valid: bool, card_nest: list[list[playing_cards.Card]]) -> bool:
            """Returns `valid` parameter as a way to check if the function executed successfully. If so, removes the played cards from `considered_cards` and adds them to `played_cards`."""
            if valid:
                for cards in card_nest:
                    played_cards.add_several_to_top_of_deck(cards)
                    for card in cards:
                        considered_cards.remove_specific(card)
            return valid
        
        if validate_and_remove(contains_pairs, pairs):
            print("You played pairs!")
        elif validate_and_remove(contains_straights, straights):
            print("You played straights!")
        else:
            print("I hope you wanted to discard those!")
            discard.add_several_to_top_of_deck(considered_cards.empty_deck())
        pause()

    discard.add_several_to_top_of_deck(hand.empty_deck())
    score_discard = len(discard.cards)
    score_played = len(played_cards.cards)
    score = score_played - score_discard
    print("And that's the game!\nYour remaining cards have been discarded.")
    print(f"Your final score is {score}. {"Good job!" if score > 0 else "Better luck next time!"}\nBreakdown:\n- {score_played} played cards\n- Minus {score_discard} discared cards\n- Equals {score} points")
    print("Thanks for playing!")
    pause()

def main(mode: str) -> None:
    if mode == "graphics":
        graphics_game_loop()
    if mode == "text":
        text_game_loop()
    return

if __name__ == "__main__":
    # pick game-mode from argument
    parser = argparse.ArgumentParser(description="Play Despair: A Game About Debt")
    parser.add_argument("--mode", type=str, choices=["graphics", "text"], default="graphics", help="Choose the game mode: 'graphics' for graphical interface, 'text' for text-based interface")
    args = parser.parse_args()
    main(args.mode)