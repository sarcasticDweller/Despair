from pygame import Surface, Rect, time, display, font, mouse
from pygame import init as pinit
from pygame.sprite import Sprite
from pygame import quit as pquit
from typing import Iterator, List, Tuple, Callable, Any, Iterable
from src.constants import  COLOR_KEY
from src.gopher import resolve_image
from enum import Flag, auto



class EventFlags(Flag): # event flags arent going to be a universal thing, so this probably shouldnt live here. honestly, i want to make mini_pygame its own module at some point
    QUIT = auto()
    MOUSE_CLICK = auto()

"""
I'm hitting a snag with how I want to interpret Pygame events. Pygame interprets keyboard, mouse, and window events. I want to turn those into *game* evenets. A mouse-click should signal a selecting action, a keyboard event should signal a movement action, etc. etc
"""

class Game:
    class ExitCodes(Flag):
        GOOD = auto()
        BAD = auto()
        WINDOW_CLOSED = auto()

    def __init__(
            self,
            window: Surface,
            bg_color: Tuple[int, int, int],
            fps: int,
            updatables: "Group",
            drawables: "Group",
            event_handler: Callable[[], EventFlags],
    ):
        self.window, self.bg_color = window, bg_color
        self.clock = Clock(fps)
        self.updatables, self.drawables = updatables, drawables
        self.event_handler = event_handler

    @classmethod
    def init(cls, window_size: tuple[int, int], caption: str = "", font_init: bool = False) -> Surface:
        """
        Starts Pygame and creates a game window. This should be called before creating a game object.
        
        :param window_size: A tuple containing the dimensions of the window.
        :type window_size: tuple[int, int]
        :param caption: Sets the window's caption. 
        :type caption: str (optional)
        :param font_init: Allows initializing pygame's font module. Set to False by default.
        :type font_init: bool (optional)
        :return: Description
        :rtype: Surface
        """
        pinit()
        if font_init:
            font.init()
        window = display.set_mode(window_size)
        if len(caption) > 0:
            display.set_caption(caption)
        return window
    
    def tick(self) -> ExitCodes:
        flags = self.event_handler()
        if EventFlags.QUIT in flags:
            pquit()
            return Game.ExitCodes.WINDOW_CLOSED
        if EventFlags.MOUSE_CLICK in flags: #remove me!
            print("Game saw the mouse-click")

        self.clock.update()
        self.updatables.update(flags)
        self.draw()
        return Game.ExitCodes.GOOD

    def draw(self):
        self.window.fill(self.bg_color)
        self.drawables.draw(self.window)
        display.flip()
        

    
class Clock:
    """A wrapper for pygame's clock library, designed to make the clock *almost*-but-not-quite a sprite"""
    def __init__(self, fps: int):
        self._clock = time.Clock()
        self._fps = fps
        self.dt = 0
    
    def update(self) -> None:
        self.dt = self._clock.tick(self._fps) / 1000

class Prototype(Sprite):
    def __init__(self):
        super().__init__()
        # i *think* these are necessary, but i'm really not sure
        self.image = Surface((0, 0))
        self.rect = self.image.get_rect()
        self.x, self.y = 0, 0
    
    def set_sprite_image(self, path_to_image: str, color_key: tuple[int, int, int]) -> None:
        self.image = resolve_image(path_to_image, color_key)
        self.rect = self.image.get_rect()
    
    def place_sprite_image(self, x: int, y: int) -> None:
        self.x, self.y = x, y
    
    def move_sprite_image(self) -> None:
        """(UNIMPLEMENTED) Uses vector logic to move the sprite around. Woo, floating numbers!"""
        pass
    
    # these functions should be obscured by the classes that inheret Prototype
    
    def update(self, flags: EventFlags = EventFlags(0)) -> None: # i think i want this to take a delta-time variable but im really not there yet
        self.rect.x, self.rect.y = self.x, self.y

    def draw(self, surface: Surface) -> None:
        surface.blit(
            self.image, 
            (self.rect.x, self.rect.y)
        )
    
    def collide(self, *others: "Prototype") -> List["Prototype"]: # still no clue why the quotes make pyright happy
        collided_sprites: List["Prototype"] = []
        me = self.rect
        for sprite in others:
            it = sprite.rect
            # thank you https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection for saving me from the effort of remembering how to do rectangular collisions
            if me.x < it.x + it.width and \
                me.x + me.width > it.x and \
                me.y < it.y + it.height and \
                me.y + me.height > it.y:
                collided_sprites.append(sprite)
            
        return collided_sprites

class MouseSprite(Prototype):
    def __init__(self):
        super().__init__()
    
    def update(self, flags: EventFlags = EventFlags(0)) -> None:
        self.x, self.y = mouse.get_pos()
        super().update(flags)

class FontSprite(Prototype): 
    """A wrapper for pygame's font library. FontSprites *should* be somewhat compatible with strings. They support the following actions:
    - repr
    - len
    - bool
    - iter
    
    Missing Features:\n
    Operator	Description\n
    `==`	Equal\n
    `!=`	Not equal\n
    `>`	Greater than\n
    `<`	Less than\n
    `>=`	Greater than or equal to\n
    `<=`	Less than or equal to\n
    `+`	Concatenation\n
    `*`	Repetition\n
    `in`	Membership\n
    `not in`	Not membership\n

    TBH though, I don't know what strings in Python support. That list of missing features is AI-generated.

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
            raise Exception("Font not initialized before creation of FontSprite")
        
        self._font = font.SysFont(font_name, font_size)
        self._text = text
        self._anti_aliasing = anti_aliasing
        self._text_color = text_color
        self._background_color = background_color
        self.update() # this should work, right?
        self.x, self.y = coords
    
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
    
    def update(self, flags: EventFlags = EventFlags(0)) -> None:
        self.image = self._font.render(
            self._text,
            self._anti_aliasing,
            self._text_color,
            self._background_color
        )
        self.rect = self.image.get_rect()
        super().update()

# im going insane. pygame is stupid. pyright is stupid. i just need something to *work*

# re: insanity,
# instead of using the group class pygame gives me, let's just make one that functions more or less the same but with all the type annotations my little heart could desire

class Group(List[Prototype]): # no, not a pygame group! but has similar abilities to a pygame group
    def __init__(self, *sprites: Prototype):
        """
        An almost-completely-comparable group to a typical pygame group, forged out of frustration with pyright. **Note that this group does NOT support passing iterators through `*sprites` parameters.**

        Actually, I think I want to make these groups only compatible with Prototypes, but I'm not sure of the feesability of that yet.
        
        :param sprites: Native pygame sprites or objects that inheret from pygame sprites.
        :type sprites: pygame.Sprite
        """
        super().__init__(sprites)
        #self._sprites = [*sprites] # i generally dislike *args and **kwargs, but lets just use them for simplicity forn now

    # given that this is a recreation of pygame's pygame.sprite.Group() class its worth noting some limitations. the manual (https://www.pygame.org/docs/ref/sprite.html) CLEARLY states that the *sprites argument in future functions can take an iterator containing sprites, but im not toooo sure if that works here. by my understanding, **it does not work**
    
    def extend(self, sprites: Iterable[Prototype]) -> None:
        """Only extends values not already in the group"""
        self.extend(sprite for sprite in sprites if sprite not in self)
    
    def has(self, *sprites: Prototype) -> bool:
        return all(sprite in self for sprite in sprites)
    
    def update(self, flags: EventFlags = EventFlags(0)) -> None: # to be overwritten
        for sprite in self:
            sprite.update()

    def draw(self, Surface: Surface, bgsurf: Surface | None = None, special_flags = 0) -> list[Rect]: # type: ignore
        """Draws all sprites in group. Note that arguments `bgsurf` and `special_flags` are unimplemented"""
        for sprite in self:
            Surface.blit(sprite.image, (sprite.rect.x, sprite.rect.y)) # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType, reportUnknownArgumentType]
            # whoops!

    def clear(self, Surface_dest: Surface, background: Surface) -> None: # type: ignore
        # see https://github.com/pygame/pygame/blob/main/src_py/sprite.py#L357 (AbstractGroup.clear()) for what to rip off
        pass

    def empty(self) -> None:
        self._sprites = []

class GroupGroup(List[Group]): # brilliant name there
    def __init__(self, *groups: Group):
        super().__init__(*groups)
    
    def update(self, *args: Any) -> None: 
        for group in self:
            group.update(*args) 