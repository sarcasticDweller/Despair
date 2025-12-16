import pygame  # pyright: ignore[reportMissingTypeStubs]
from constants import *

def _update(dt, updatable) -> None:
    for sprite in updatable:
        sprite.update(dt)

def _draw(screen: pygame.Surface, drawable) -> None:
    for sprite in drawable:
        sprite.draw(screen)
    pygame.display.flip()

def main() -> None:
    # Initialize Pygame
    print("Starting game...")
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # pyright: ignore[reportUnusedVariable]
    pygame.display.set_caption(WINDOW_CAPTION)
    clock = pygame.time.Clock() # pyright: ignore[reportUnusedVariable]
    dt = 0 # pyright: ignore[reportUnusedVariable]
    fps = FPS  # pyright: ignore[reportUnusedVariable]

    # Initialize sprite groups
    updatable = pygame.sprite.Group()  # pyright: ignore[reportUnknownVariableType, reportUnusedVariable]
    drawable = pygame.sprite.Group()  # pyright: ignore[reportUnknownVariableType, reportUnusedVariable]
    player_cards = pygame.sprite.Group()  # pyright: ignore[reportUnknownVariableType, reportUnusedVariable]

    # Initialize test sprite
    heart = pygame.image.load("assets/heart.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        # draw the heart
        _update(dt, updatable)
        _draw(screen, drawable)