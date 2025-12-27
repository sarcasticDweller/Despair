import argparse # pyright: ignore[reportMissingTypeStubs]
from src.text_game import game_loop as text_game_loop
from src.graphics_game import game_loop as graphics_game_loop

if __name__ == "__main__":
    # pick game-mode from argument
    parser = argparse.ArgumentParser(description="Play Despair: A Game About Debt")
    parser.add_argument("--mode", type=str, choices=["graphics", "text"], default="graphics", help="Choose the game mode: 'graphics' for graphical interface, 'text' for text-based interface")
    mode = parser.parse_args().mode

    print(f"Starting Despair in \"{mode}\" mode.")
    if mode == "graphics":
        graphics_game_loop()
    elif mode == "text":
        text_game_loop()
    else:
        raise Exception("Invalid game \"mode\" selected.")