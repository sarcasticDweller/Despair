from pygame import sprite, Surface, image, Rect
from typing import Iterator, List
from src.constants import  COLOR_KEY
from src.gopher import resource_path

def resolve_image(path: str) -> Surface:  
    img: Surface = image.load(resource_path(path)).convert() 
    img.set_colorkey(COLOR_KEY)
    return img

class Prototype(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Surface((1, 1))
        self.rect = self.image.get_rect()
    
    def move_rect(self, x: int = 0, y: int = 0) -> None:
        self.rect.x += x
        self.rect.y += y
    
    # these functions should be obscured by the classes that inheret Prototype
    
    def update(self, dt: float):
        pass

    def draw(self):
        pass

# im going insane. pygame is stupid. pyright is stupid. i just need something to *work*

# re: insanity,
# instead of using the group class pygame gives me, let's just make one that functions more or less the same but with all the type annotations my little heart could desire

class Group(): # no, not a pygame group! but has the same abilities as a pygame group
    def __init__(self, *sprites: sprite.Sprite):
        self._sprites = [*sprites] # i generallyl dislike *args and **kwargs, but lets just use them for simplicity forn now
    
    def __contains__(self, sprite: sprite.Sprite) -> bool:
        return sprite in self._sprites
    
    def __len__(self) -> int:
        return len(self._sprites)
    
    def __bool__(self) -> bool:
        return len(self) > 0 # this should work fine, right?
    
    def __iter__(self) -> Iterator[sprite.Sprite]:
        return iter(self._sprites)
    
    def sprites(self) -> List[sprite.Sprite]:
        return self._sprites

    
    def copy(self) -> "Group":
        return Group(*self._sprites)
    
    # given that this is a recreation of pygame's pygame.sprite.Group() class its worth noting some limitations. the manual (https://www.pygame.org/docs/ref/sprite.html) CLEARLY states that the *sprites argument in future functions can take an iterator containing sprites, but im not toooo sure if that works here. good thing we have unittest
    
    def add(self, *sprites: sprite.Sprite) -> None:
        self._sprites.extend(sprite for sprite in sprites if sprite not in self)
    
    def remove(self, *sprites: sprite.Sprite) -> None:
        self._sprites = [sprite for sprite in self if sprite not in sprites]
    
    def has(self, *sprites: sprite.Sprite) -> bool:
        return all(sprite in self for sprite in sprites)
    
    def update(self, *args, **kwargs) -> None: # pyright: ignore[reportUnknownParameterType, reportMissingParameterType]
        """Updates all sprites in the group. Note that all sprites must take the same arguments in their update command"""
        for sprite in self:
            sprite.update(*args, **kwargs)

    def draw(self, Surface: Surface, bgsurf: Surface | None = None, special_flags = 0) -> list[Rect]: # type: ignore
        """Draws all sprites in group. Note that arguments `bgsurf` and `special_flags` are unimplemented"""
        for sprite in self:
            Surface.blit(sprite.image, (sprite.rect.x, sprite.rect.y)) # pyright: ignore[reportUnknownMemberType, reportUnknownArgumentType]

    def clear(self, Surface_dest: Surface, background: Surface) -> None:
        pass

    def empty(self) -> None:
        self._sprites = []
