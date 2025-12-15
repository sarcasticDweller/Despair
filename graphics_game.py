import pygame  # pyright: ignore[reportMissingTypeStubs]
from constants import *

def graphics_game_loop() -> None:
    # Initialize Pygame
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
        screen.fill((0, 0, 0))  # Clear the screen with black
        screen.blit(heart, (WINDOW_WIDTH // 2 - heart.get_width() // 2, WINDOW_HEIGHT // 2 - heart.get_height() // 2))
        pygame.display.flip()