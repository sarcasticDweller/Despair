import pygame
import src.playing_cards as pc
from src.constants import SUIT_PATHS, CARD_PATHS
from src.gopher import resource_path


class CardSprite(pygame.sprite.Sprite):

    def __init__(self, card: pc.Card, facing_up: bool = False):
        super().__init__()
        self.facing_up = facing_up
        self.card_data = card

        # create the suit
        self.suit_image: pygame.Surface = pygame.image.load(resource_path(SUIT_PATHS[card.suit])).convert() 
        self.suit_image.set_colorkey((255, 255, 255)) # write code that works before you code that's good

        # create the card body
        self.card_image_front: pygame.Surface = pygame.image.load(resource_path(CARD_PATHS["front"]))
        self.card_image_back: pygame.Surface = pygame.image.load(resource_path(CARD_PATHS["back"]))
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
        base_image = images[0]
        for img in images[1:]:
            base_image.blit(img, (0, 0)) # you "blit" images to a surface, which can be drawn later. i *think*
        return base_image