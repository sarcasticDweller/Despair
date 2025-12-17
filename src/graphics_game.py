import pygame  # pyright: ignore[reportMissingTypeStubs]
from constants import *
import cards_with_graphics
import playing_cards

# oh no, i dont know what im doing! unfortunately, i have to write this in a github codespace and build it for a windows environment with no pygame installed locally before i can test things, so development is going to be slow and painful. happy happy joy joy.

# okay, pyright is incredibly upset, but i need to test *something*

class aaah: # type: i dont heckin know
    pass

def _update(dt: int, sprites: aaah) -> None: # trying to type "sprites" is absolutely breaking me

    # should hold collider logic too, eh?
    for sprite in sprites:
        sprite.update(dt)
    
def _draw(surface: pygame.Surface, sprites) -> None:
    surface.fill(BG_COLOR)
    for sprite in sprites:
        sprite.draw(surface)
    pygame.display.flip()

def main() -> None:
    # initialize pygame
    pygame.init()
    window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # gonna add extra type hints to help learn pygame (and to make pyright happy)
    pygame.display.set_caption(WINDOW_CAPTION)

    # initialize clock
    clock = pygame.time.Clock()
    dt = 0
    fps = FPS

    # initialize groups, with questionable typing
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    # test card
    card = cards_with_graphics.CardSprite(STOCK_CARD)
    drawables.add(card)

    # game loop
    while True:
        for event in pygame.event.get():
            # makes the close button work
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        dt = clock.tick(fps) / 1000 # magic number converts to seconds
        _update(dt, updatables)
        _draw(window, drawables)
