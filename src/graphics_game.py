import pygame  # pyright: ignore[reportMissingTypeStubs]
from src.constants import *
import src.cards_with_graphics

# oh no, i dont know what im doing! unfortunately, i have to write this in a github codespace and build it for a windows environment with no pygame installed locally before i can test things, so development is going to be slow and painful. happy happy joy joy.


def main() -> None:
    # initialize pygame
    pygame.init()
    window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # gonna add extra type hints to help learn pygame (and to make pyright happy)
    pygame.display.set_caption(WINDOW_CAPTION)

    # initialize clock
    clock = pygame.time.Clock()
    dt = 0 # pyright: ignore[reportUnusedVariable]
    fps = FPS

    # initialize groups, with questionable typing
    updatables = pygame.sprite.Group() # pyright: ignore[reportUnknownVariableType, reportUnusedVariable]
    drawables = pygame.sprite.Group() # pyright: ignore[reportUnknownVariableType]

    card1 = src.cards_with_graphics.CardSprite(STOCK_CARD, True)
    card2 = src.cards_with_graphics.CardSprite(STOCK_CARD, True)
    updatables.add(card1) # pyright: ignore[reportUnknownMemberType]
    # test hand
    hand = src.cards_with_graphics.HandOfCards((100, 100), [card1, card2])
    #updatables.add(hand) # pyright: ignore[reportUnknownMemberType]
    drawables.add(hand) # pyright: ignore[reportUnknownMemberType]


    # prototype game loop
    while True:
        for event in pygame.event.get():
            # makes the close button work
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                card1.flip_card()
        dt = clock.tick(fps) / 1000 # pyright: ignore[reportUnusedVariable] # magic number converts to seconds
        drawables.draw(window)
        updatables.update(dt)
        pygame.display.flip()
