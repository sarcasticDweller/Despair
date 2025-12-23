from src.playing_cards import Suit, Rank, Card # importing these because the paths rely on the enums

# Game window
WINDOW_WIDTH = 200
WINDOW_HEIGHT = 200
WINDOW_CAPTION = "Despair: A Game About Debt"
FPS = 60
BG_COLOR = (255, 255, 255)
FONT_TYPE = "Arial"
FONT_SIZE = 20

# Game Rules
HAND_SIZE = 5
STARTING_DECK_FRACTION = 0.5

# usefuls
STOCK_CARD = Card(Suit.HEART, Rank.ACE)
COLOR_KEY = (255, 255, 255)


# file paths
# hey, wouldnt these paths make more sense as enums?

SUIT_PATHS = {
    Suit.SPADE: "assets/card/suit/devsprite_spade.png",
    Suit.HEART: "assets/card/suit/devsprite_heart.png",
    Suit.CLUB: "assets/card/suit/devsprite_club.png",
    Suit.DIAMOND: "assets/card/suit/devsprite_diamond.png"
}

RANK_PATHS = {
    Rank.ACE: "assets/card/rank/devsprite_ace.png",
    Rank.TWO: "assets/card/rank/devsprite_deuce.png",
    Rank.THREE: "assets/card/rank/devsprite_three.png",
    Rank.FOUR: "assets/card/rank/devsprite_four.png",
    Rank.FIVE: "assets/card/rank/devsprite_five.png",
    Rank.SIX: "assets/card/rank/devsprite_six.png",
    Rank.SEVEN: "assets/card/rank/devsprite_seven.png",
    Rank.EIGHT: "assets/card/rank/devsprite_eight.png",
    Rank.NINE: "assets/card/rank/devsprite_nine.png",
    Rank.TEN: "assets/card/rank/devsprite_ten.png",
    Rank.JACK: "assets/card/rank/devsprite_jack.png",
    Rank.QUEEN: "assets/card/rank/devsprite_queen.png",
    Rank.KING: "assets/card/rank/devsprite_king.png"
}

CARD_PATHS = {
    "front": "assets/card/devsprite_card_front.png",
    "back": "assets/card/devsprite_card_back.png",
    "error": "assets/card/devsprite_card_error.png"
}