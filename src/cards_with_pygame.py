import pygame
import playing_cards as pc

# constants, to move to constants file *later*
SUIT_PATHS = {
    pc.Suit.SPADE: "../assets/card/devsprite_spade.png",
    pc.Suit.HEART: "../assets/card/devsprite_heart.png",
    pc.Suit.CLUB: "../assets/card/devsprite_club.png",
    pc.Suit.DIAMOND: "../assets/card/devsprite_diamond.png"
}

class CardSprite(pygame.sprite.Sprite):
    def __init__(self, card: pc.Card, facing_up: bool = False):
        super().__init__()
        self.facing_up = facing_up

        # create the suit
        self.suit_image: pygame.Surface = pygame.image.load(SUIT_PATHS[card.suit]) # will throw an error if it receives a bad suit (or by extension a bad card)
        self.suit_rect: pygame.Rect = self.suit_image.get_rect()

        # create the card body
        self.card_image_front: pygame.Surface = pygame.image.load("../assets/card/devsprite_card_front.png")
        self.card_image_back: pygame.Surface = pygame.image.load("../assets/card/devsprite_card_back.png")
        # okay, i have images, now where to shove them...
        if self.facing_up:
            self.card_image = self.card_image_front
        else:
            self.card_image = self.card_image_back
        self.card_rect = self.card_image.get_rect()

    
    def flip_card(self) -> None:
        self.facing_up = not self.facing_up
    
