from src.constants import *
from src.cards_with_graphics import CardSprite, HandOfCards
from src.playing_cards import Card, Suit, Rank
from src.mini_pygame import FontSprite, Group, Game, EventFlags
from pygame import event
import pygame
from typing import Tuple

def initializer() -> Tuple[Group, Group]:
    card1 = CardSprite(STOCK_CARD, (10, 20), True)
    card2 = CardSprite(Card(Suit.SPADE, Rank.TWO), (40, 10), True)
    hand = HandOfCards(card1, card2)
    message = FontSprite(FONT_TYPE, FONT_SIZE, text="Hello world", coords=(30, 30))
    updatables = Group(*hand.sprites(), message)
    drawables = updatables.copy()
    return updatables, drawables

def event_handler() -> EventFlags:  
    flags = EventFlags(0)
    for e in event.get():
        if e.type == pygame.QUIT:
            flags |= EventFlags.QUIT
        if e.type == pygame.MOUSEBUTTONDOWN:
            flags |= EventFlags.MOUSE_CLICK
        # if e.type == specific_key_pressed: flags |= EventFlags.MOVE_LEFT, or something like that
    return flags

def game_loop() -> None:
    window = Game.init(
        (WINDOW_WIDTH, WINDOW_HEIGHT),
        WINDOW_CAPTION,
        font_init=True
    )
    print("initialized window")
    updatables, drawables = initializer()
    print("initialized items")
    game = Game(
        window,
        BG_COLOR,
        FPS,
        updatables,
        drawables,
        event_handler
    )
    print("initialized game instance")
    while True:
        event = game.tick()
        if event == game.ExitCodes.WINDOW_CLOSED:
            break
    print("Ending game")
    return
