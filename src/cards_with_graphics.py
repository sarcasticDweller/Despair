from pygame import Surface 
import src.playing_cards as pc
from src.constants import SUIT_PATHS, CARD_PATHS, RANK_PATHS, COLOR_KEY
from src.mini_pygame import Prototype, MouseSprite, Group, EventFlags
from src.gopher import resolve_image, resolve_images

class CardSprite(Prototype):
    def __init__(self, card: pc.Card, coords: tuple[int, int], facing_up: bool = True) -> None: 
        super().__init__()
        self.facing_up = facing_up
        self.card_data = card
        self.image_front = self._card_face
        self.image_back = resolve_image(CARD_PATHS["back"], COLOR_KEY)
        self.x, self.y = coords
        
        # necessary sprite attributes
        self.image = self._card_side_showing
        self.rect = self.image.get_rect()
    
    def update(self, flags: EventFlags = EventFlags(0)) -> None: # pyright: ignore[reportIncompatibleMethodOverride]
        super().update()
        if EventFlags.MOUSE_CLICK in flags:
            self.flip_card()
        self.image = self._card_side_showing
    
    def flip_card(self) -> None:
        """Indirectly swaps the card's image to show front or back"""
        self.facing_up = not self.facing_up
    
    @property # just learned what these do!
    def _card_side_showing(self) -> Surface:
        """Returns the appropriate image based on which way the card is facing"""
        return self.image_front if self.facing_up else self.image_back

    @property # yep, im going to have way too much fun with these
    def _card_face(self) -> Surface: # customize me later when you evolve from devsprites!
        card = self.card_data
        suit, rank, front = resolve_images(
            COLOR_KEY,
            SUIT_PATHS[card.suit],
            RANK_PATHS[card.rank],
            CARD_PATHS["front"],
        )
        slots = {
            "top": {
                rank: (0, 0),
                suit: (rank.get_width(), 0)
            },
            "bottom": { # make sure you arent out of bounds!
                rank: (front.get_width() - rank.get_width(), front.get_height() - rank.get_height()),
                suit: (front.get_width() - rank.get_width() - suit.get_width(), front.get_height() - suit.get_height())
            }
        }
        front.blits((
            (suit, slots["top"][suit]),
            (suit, slots["bottom"][suit]),
            (rank, slots["top"][rank]),
            (rank, slots["bottom"][rank]),
        ))
        return front

class HandOfCards(Group):
    def __init__(self, *cards: CardSprite):
        super().__init__(*cards)
    
    def update(self, flags: EventFlags = EventFlags(0)) -> None:
        #super().update()
        #return
        # oh dear, you add one little feature and the world catches on fire. i cant tell *why* but now all the cards are being drawn in the CORNER *facepalm*
        if EventFlags.MOUSE_CLICK in flags:
            print("Click detected!")
            mouse = MouseSprite() # a temporary one!
            mouse.update()
            clicked_cards = mouse.collide(*self)
            if clicked_cards:
                for card in clicked_cards:
                    flags_to_pass = EventFlags(0)
                    flags_to_pass |= EventFlags.MOUSE_CLICK
                    card.update(flags_to_pass)
        for card in self:
            card.update()
            
