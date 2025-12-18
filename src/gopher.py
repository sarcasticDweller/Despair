import os, sys

def resource_path(relative_path: str) -> str:
    """Vibe coding time. I'm sorry Dad. Returns the absolute path to a resource, works for both development and cx_Freeze. """
    try:
        base_path = sys._MEIPASS   # pyright: ignore[reportUnknownVariableType, reportAttributeAccessIssue, reportUnknownMemberType]
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path) # pyright: ignore[reportUnknownArgumentType]