from src.constants import *
import src.cards_with_graphics, src.playing_cards
import src.mini_pygame as mp
from pygame import quit as pquit

def main() -> None: # i know i can make this tighter... i KNOW i can
    window = mp.initialize_pygame(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_CAPTION)
    clock = mp.Clock(FPS)

    card1 = src.cards_with_graphics.CardSprite(STOCK_CARD, (10, 20), True)
    card2 = src.cards_with_graphics.CardSprite(src.playing_cards.Card(
        src.playing_cards.Suit.SPADE,
        src.playing_cards.Rank.TWO
    ), (40, 10), True)
    hand = src.cards_with_graphics.HandOfCards(card1, card2)
    message = mp.FontSprite(FONT_TYPE, FONT_SIZE, text="Hello world", coords=(30, 30))
    drawables = mp.Group(message)

    
    groups_to_draw: list[mp.Group] = [hand, drawables] # the more robust way to do this would be to make a group "drawables" that can inheret members from other groups

    while True:
        flags = mp.event_handler()
        if mp.EventFlags.QUIT in flags:
            pquit()
            return
        clock.update()
        mp.draw(window, BG_COLOR, *groups_to_draw)

import pygame
def side() -> None:
    pygame.font.init()
    pass
    """
    pygame.font.init()
    my_font = pygame.font.SysFont("Arial", 20)
    text_surface = my_font.render("hello world", False, (0, 0, 0))
    """


