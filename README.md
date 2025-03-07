# Uno Simulator 🃏

This project is a Python-based simulation of the classic UNO card game, where multiple bots compete against each other. The game follows standard UNO rules with a deck containing color cards (red, blue, yellow, green) and special cards (reverse, skip, +2, +4, wild). It features automated bot moves, card abilities, and a simple user interface to set up the game.

## Features

- **Automated Gameplay**: Bots play against each other by selecting cards based on the current face card and available deck.
- **Standard UNO Deck**: Supports regular cards (0-9) and special cards (reverse, skip, +2, +4, wild) in four colors, plus special action cards.
- **Card Abilities**: Implements special abilities like skipping turns, reversing order, and making opponents pick cards.
- **Error Handling**: Validates user input for the number of bots and delay time to ensure smooth gameplay.
- **Dynamic Difficulty**: Randomized bot behavior for saying "UNO", adding a challenge element.
- **Extensibility**: The code structure allows easy modifications for adding more features or customizing bot behavior.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Kinglord1090/uno-simulator.git
    ```
2. Navigate to the project folder:
    ```bash
    cd uno-simulator
    ```

## Usage

1. Run the script:
    ```bash
    python uno-simu.py
    ```
2. Enter the number of cards to be dealt, the number of bots (maximum 10), and the delay between each move.
3. Watch the bots play against each other until one bot finishes all cards.
4. The program displays the winner's list and the total game duration.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
  
- Inspired by the original UNO game and various card game simulators.
- Thanks to Python’s `random` module for handling deck shuffling and card distribution.
