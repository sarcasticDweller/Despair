import pygame
import playing_cards as pc

# constants, to move to constants file *later*

# these paths are causing errors depending on where theyre run from. im starting to suspect that this is a bad way to manage pathing
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
        self.card_data = card

        # create the suit
        self.suit_image: pygame.Surface = pygame.image.load(SUIT_PATHS[card.suit]).convert() 
        self.suit_image.set_colorkey((255, 255, 255)) # write code that works before you code that's good

        # create the card body
        self.card_image_front: pygame.Surface = pygame.image.load("../assets/card/devsprite_card_front.png")
        self.card_image_back: pygame.Surface = pygame.image.load("../assets/card/devsprite_card_back.png")
        # okay, i have images, now where to shove them...
        if self.facing_up:
            self.card_image = self.card_image_front
        else:
            self.card_image = self.card_image_back
        
        # necessary sprite attributes
        self.image = self.layer_images_and_return_single_sprite([self.card_image, self.suit_image])
        self.rect = self.image.get_rect()

    
    def flip_card(self) -> None:
        self.facing_up = not self.facing_up
    
    def layer_images_and_return_single_sprite(self, images: list[pygame.Surface]) -> pygame.Surface:
        # layer your images later
        base_image = images[0]
        for img in images[1:]:
            base_image.blit(img, (0, 0)) # you "blit" images to a surface, which can be drawn later. i *think*
        return base_image