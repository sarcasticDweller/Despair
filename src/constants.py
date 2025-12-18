from src.playing_cards import Suit, Rank, Card # importing these because the paths rely on the enums

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
STOCK_CARD = Card(Suit.HEART, Rank.ACE)


# file paths

SUIT_PATHS = {
    Suit.SPADE: "assets/card/devsprite_spade.png",
    Suit.HEART: "assets/card/devsprite_heart.png",
    Suit.CLUB: "assets/card/devsprite_club.png",
    Suit.DIAMOND: "assets/card/devsprite_diamond.png"
}

CARD_PATHS = {
    "front": "assets/card/devsprite_card_front.png",
    "back": "assets/card/devsprite_card_back.png"
}