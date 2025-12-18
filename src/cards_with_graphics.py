import pygame
import src.playing_cards as pc
from src.constants import SUIT_PATHS, CARD_PATHS, RANK_PATHS, COLOR_KEY
from src.gopher import resource_path

def resolve_img(path: str) -> pygame.Surface:  
    img: pygame.Surface = pygame.image.load(resource_path(path)).convert() 
    img.set_colorkey(COLOR_KEY)
    return img

class CardSprite(pygame.sprite.Sprite):

    def __init__(self, card: pc.Card, facing_up: bool = False):
        super().__init__()
        self.facing_up = facing_up
        self.card_data = card

        # get image data
        self.suit_image = resolve_img(SUIT_PATHS[card.suit])
        self.rank_image = resolve_img(RANK_PATHS[card.rank])
        self.card_image_front = resolve_img(CARD_PATHS["front"])
        self.card_image_front = self._design_card_face()
        self.card_image_back = resolve_img(CARD_PATHS["back"])
        
        # necessary sprite attributes
        self.image = self._card_side_showing
        self.rect = self.image.get_rect()
    
    def update(self, dt: float) -> None:
        self.image = self._card_side_showing
    
    def flip_card(self) -> None:
        """Indirectly swaps the card's image to show front or back"""
        self.facing_up = not self.facing_up
    
    @property # just learned what these do!
    def _card_side_showing(self) -> pygame.Surface:
        """Returns the appropriate image based on which way the card is facing"""
        return self.card_image_front if self.facing_up else self.card_image_back

    def _design_card_face(self) -> pygame.Surface:
        """Adds suit and rank images to the card face and returns the final image. Should also add pips later."""
        base = self.card_image_front
        suit = self.suit_image
        rank = self.rank_image
        corner_slots = {
            "suit": {
                "top": (0, 0),
                "bottom": (
                    base.get_width() - suit.get_width(),
                    base.get_height() - suit.get_height()
                )
            },
            "rank": {
                "top": (suit.get_width(), 0),
                "bottom": (
                    base.get_width() - suit.get_width() - rank.get_width(), 
                    base.get_height() - suit.get_height() 
                )
            }
        }

        base.blit(suit, corner_slots["suit"]["top"])
        base.blit(suit, corner_slots["suit"]["bottom"])
        base.blit(rank, corner_slots["rank"]["top"])
        base.blit(rank, corner_slots["rank"]["bottom"])

        return base

class HandOfCards(pygame.sprite.Sprite):
    """Holds x cards and controls how to render them based on its dimensions. Attempts to render all cards possible"""

    def __init__(self, rect: tuple[int, int], cards: list[CardSprite]):
        self.cards = cards
        self.backdrop = pygame.Surface(rect)

        # necessary sprite atributes
        self.image: pygame.Surface = pygame.Surface((0, 0))
        self.rect = self.image.get_rect()

    def update(self):
        # blit all of self.cards to self.image
        pass
