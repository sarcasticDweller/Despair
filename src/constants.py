import src.playing_cards as pc
import sys, os

# hey, wait a second, this is supposed to be a constants file! (don't worry, we'll get rid of the code once the damn thing compiles without a runtime error literally once)

# Game window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
WINDOW_CAPTION = "Despair: A Game About Debt"
FPS = 60
BG_COLOR = (255, 255, 255)

# Game Rules
HAND_SIZE = 5
STARTING_DECK_FRACTION = 0.5

# usefuls
STOCK_CARD = pc.Card(pc.Suit.HEART, pc.Rank.ACE)

def resource_path(relative_path):
    """ Returns the absolute path to a resource, works for both development and cx_Freeze. """
    try:
        base_path = sys._MEIPASS  # This is set when using cx_Freeze
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# file paths
# these paths are causing errors depending on where theyre run from. im starting to suspect that this is a bad way to manage pathing
SUIT_PATHS = {
    # Using absolute paths to avoid pathing issues
    pc.Suit.SPADE: resource_path("assets/card/devsprite_spade.png"),
    pc.Suit.HEART: resource_path("assets/card/devsprite_heart.png"),
    pc.Suit.CLUB: resource_path("assets/card/devsprite_club.png"),
    pc.Suit.DIAMOND: resource_path("assets/card/devsprite_diamond.png")
}
CARD_PATHS = {
    "front": resource_path("assets/card/devsprite_card_front.png"),
    "back": resource_path("assets/card/devsprite_card_back.png")
}