from pygame import Surface 
import src.playing_cards as pc
from src.constants import SUIT_PATHS, CARD_PATHS, RANK_PATHS
from src.mini_pygame import Prototype, Group, resolve_image



# some lessons we're learning: pyright and pygame do NOT get along. its going to be a challenge to not let this deter me

class CardSprite(Prototype):
    def __init__(self, card: pc.Card, coords: tuple[int, int], facing_up: bool = True) -> None: 
        super().__init__()
        self.facing_up = facing_up
        self.card_data = card

        # get image data
        self.suit_image = resolve_image(SUIT_PATHS[card.suit])
        self.rank_image = resolve_image(RANK_PATHS[card.rank])
        self.card_image_front = resolve_image(CARD_PATHS["front"])
        self.card_image_front = self._design_card_face()
        self.card_image_back = resolve_image(CARD_PATHS["back"])
        
        # necessary sprite attributes
        self.image = self._card_side_showing
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coords
    
    def update(self, dt: float) -> None:
        self.image = self._card_side_showing
    
    def flip_card(self) -> None:
        """Indirectly swaps the card's image to show front or back"""
        self.facing_up = not self.facing_up
    
    @property # just learned what these do!
    def _card_side_showing(self) -> Surface:
        """Returns the appropriate image based on which way the card is facing"""
        return self.card_image_front if self.facing_up else self.card_image_back

    def _design_card_face(self) -> Surface:
        """Adds suit and rank images to the card face and returns the final image. Should also add pips later."""
        base = self.card_image_front
        suit = self.suit_image
        rank = self.rank_image
        corner_slots = {
            suit: {
                "top": (0, 0),
                "bottom": (
                    base.get_width() - suit.get_width(),
                    base.get_height() - suit.get_height()
                )
            },
            rank: {
                "top": (suit.get_width(), 0),
                "bottom": (
                    base.get_width() - suit.get_width() - rank.get_width(), 
                    base.get_height() - suit.get_height() 
                )
            }
        }
        base.blits((
            (suit, corner_slots[suit]["top"]),
            (suit, corner_slots[suit]["bottom"]),
            (rank, corner_slots[rank]["top"]),
            (rank, corner_slots[rank]["bottom"])
        ))

        return base
    
class HandOfCards(Group):
    def __init__(self, *cards: CardSprite):
        super().__init__(*cards)