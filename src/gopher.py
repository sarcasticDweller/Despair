import os, sys
from pygame import Surface, image
from typing import List

def resource_path(relative_path: str) -> str:
    """Vibe coding time. I'm sorry Dad. Returns the absolute path to a resource, works for both development and cx_Freeze. """
    try:
        base_path = sys._MEIPASS   # pyright: ignore[reportUnknownVariableType, reportAttributeAccessIssue, reportUnknownMemberType]
        # apparently this makes it compatible with cx_Freeze
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path) # pyright: ignore[reportUnknownArgumentType]

def resolve_image(path: str, color_key: tuple[int, int, int]) -> Surface:  
    img = image.load(resource_path(path)).convert() 
    img.set_colorkey(color_key)
    return img

def resolve_images(color_key: tuple[int, int, int], *paths: str) -> List[Surface]:
    return [resolve_image(path, color_key) for path in paths]