from pygame import Surface, Rect, time, display, event, init, font
from pygame.sprite import Sprite
from pygame.locals import QUIT
from typing import Iterator, List, Any, Tuple
from src.constants import  COLOR_KEY
from src.gopher import resolve_image
from enum import Flag, auto




class Clock:
    """A wrapper for pygame's clock library, designed to make the clock *almost*-but-not-quite a sprite"""
    def __init__(self, fps: int):
        self._clock = time.Clock()
        self._fps = fps
        self.dt = 0
    
    def update(self):
        self.dt = self._clock.tick(self._fps) / 1000

class EventFlags(Flag): # event flags arent going to be a universal thing, so this probably shouldnt live here. honestly, i want to make mini_pygame its own module at some point
    QUIT = auto()
    MOUSE_CLICK = auto()

def event_handler():  
    flags = EventFlags(0)
    for e in event.get():
        if e.type == QUIT:
            flags |= EventFlags.QUIT
    return flags

def initialize_pygame(window_width: int, window_height: int, caption: str = "") -> Surface:
    init()
    window = display.set_mode((window_width, window_height))
    display.set_caption(caption)
    return window

def draw(surface: Surface, bg_color: Tuple[int, int, int], *drawables: "Group"): 
    surface.fill(bg_color)
    for group in drawables: 
        group.draw(surface) 
    display.flip()
    

class Prototype(Sprite):
    def __init__(self):
        super().__init__()
        # i *think* these are necessary, but i'm really not sure
        self.image = Surface((1, 1))
        self.rect = self.image.get_rect()
    
    def set_sprite_image(self, path_to_image: str, color_key: tuple[int, int, int]) -> None:
        self.image = resolve_image(path_to_image, color_key)
        self.rect = self.image.get_rect()
    
    def place_sprite_image(self, x: int, y: int) -> None:
        self.rect.x, self.rect.y = x, y
    
    def move_sprite_image(self) -> None:
        """(UNIMPLEMENTED) Uses vector logic to move the sprite around. Woo, floating numbers!"""
        pass
    
    # these functions should be obscured by the classes that inheret Prototype
    
    def update(self) -> None: # i think i want this to take a delta-time variable but im really not there yet
        pass

    def draw(self, surface: Surface) -> None:
        surface.blit(
            self.image, 
            (self.rect.x, self.rect.y)
        )

class FontSprite(Prototype): 
    """A wrapper for pygame's font library. FontSprites *should* be fully compatible with strings. They support the following actions:
    - repr
    - len
    - bool
    - iter

    TBH though, I don't know what strings in Python support.

    In the future these may support fancy special effects. But not right now. 
    """
    def __init__(
            self,
            font_name: str,
            font_size: int,
            anti_aliasing: bool = False,
            text_color: tuple[int, int, int] = (0, 0, 0),
            background_color: tuple[int, int, int] = COLOR_KEY,
            text: str = "",
            coords: Tuple[int, int] = (0, 0)
        ):
        super().__init__()
        if not font.get_init():
            font.init()
        
        self._font = font.SysFont(font_name, font_size)
        self._text = text
        self._anti_aliasing = anti_aliasing
        self._text_color = text_color
        self._background_color = background_color
        self.update() # this should work, right?
        self.rect.x, self.rect.y = coords
    
    def __repr__(self) -> str:
        return self._text
    
    def __len__(self) -> int:
        return len(self._text)
    
    def __bool__(self) -> bool:
        return len(self._text) > 0
    
    def __iter__(self) -> Iterator[str]:
        return iter(self._text)
    
    def set_text(self, text: str) -> None:
        self._text = text
    
    def update(self) -> None:
        self.image = self._font.render(
            self._text,
            self._anti_aliasing,
            self._text_color,
            self._background_color
        )
        self.rect = self.image.get_rect()

# im going insane. pygame is stupid. pyright is stupid. i just need something to *work*

# re: insanity,
# instead of using the group class pygame gives me, let's just make one that functions more or less the same but with all the type annotations my little heart could desire

class Group(): # no, not a pygame group! but has similar abilities to a pygame group
    def __init__(self, *sprites: Sprite):
        self._sprites = [*sprites] # i generally dislike *args and **kwargs, but lets just use them for simplicity forn now

    def __contains__(self, sprite: Sprite) -> bool:
        return sprite in self._sprites
    
    def __len__(self) -> int:
        return len(self._sprites)
    
    def __bool__(self) -> bool:
        return len(self) > 0 # this should work fine, right?
    
    def __iter__(self) -> Iterator[Sprite]:
        return iter(self._sprites)
    
    def sprites(self) -> List[Sprite]:
        return self._sprites

    
    def copy(self) -> "Group":
        return Group(*self._sprites)
    
    # given that this is a recreation of pygame's pygame.sprite.Group() class its worth noting some limitations. the manual (https://www.pygame.org/docs/ref/sprite.html) CLEARLY states that the *sprites argument in future functions can take an iterator containing sprites, but im not toooo sure if that works here. by my understanding, **it does not work**
    
    def add(self, *sprites: Sprite) -> None:
        self._sprites.extend(sprite for sprite in sprites if sprite not in self)
    
    def remove(self, *sprites: Sprite) -> None:
        self._sprites = [sprite for sprite in self if sprite not in sprites]
    
    def has(self, *sprites: Sprite) -> bool:
        return all(sprite in self for sprite in sprites)
    
    def update(self, *args: Any, **kwargs: Any) -> None: # pyright: ignore[reportUnknownParameterType, reportMissingParameterType]
        """Updates all sprites in the group. Note that all sprites must take the same arguments in their update command"""
        for sprite in self:
            sprite.update(*args, **kwargs)

    def draw(self, Surface: Surface, bgsurf: Surface | None = None, special_flags = 0) -> list[Rect]: # type: ignore
        """Draws all sprites in group. Note that arguments `bgsurf` and `special_flags` are unimplemented"""
        for sprite in self:
            Surface.blit(sprite.image, (sprite.rect.x, sprite.rect.y)) # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType, reportUnknownArgumentType]
            # whoops!

    def clear(self, Surface_dest: Surface, background: Surface) -> None:
        pass

    def empty(self) -> None:
        self._sprites = []
