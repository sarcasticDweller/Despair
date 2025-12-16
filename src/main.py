import argparse # pyright: ignore[reportMissingTypeStubs]
from text_game import text_game_loop
from graphics_game import main as graphics_game_loop

def main(mode: str) -> None:
    if mode == "graphics":
        graphics_game_loop()
    if mode == "text":
        text_game_loop()
    return

if __name__ == "__main__":
    # pick game-mode from argument
    parser = argparse.ArgumentParser(description="Play Despair: A Game About Debt")
    parser.add_argument("--mode", type=str, choices=["graphics", "text"], default="graphics", help="Choose the game mode: 'graphics' for graphical interface, 'text' for text-based interface")
    args = parser.parse_args()
    main(args.mode)