import argparse # pyright: ignore[reportMissingTypeStubs]
import src.text_game
import src.graphics_game

def main(mode: str) -> None:
    print(f"Starting Despair in \"{mode}\" mode.")
    if mode == "graphics":
        src.graphics_game.main()
    if mode == "text":
        src.text_game.text_game_loop()
    return

if __name__ == "__main__":
    # pick game-mode from argument
    parser = argparse.ArgumentParser(description="Play Despair: A Game About Debt")
    parser.add_argument("--mode", type=str, choices=["graphics", "text"], default="graphics", help="Choose the game mode: 'graphics' for graphical interface, 'text' for text-based interface")
    args = parser.parse_args()
    main(args.mode)