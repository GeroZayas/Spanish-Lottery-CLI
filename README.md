# Spanish Lottery Number Generator

A Python application designed to generate random lottery numbers for Eurodreams, Bonoloto, and Euromillones games. Utilizing the Typer library for command-line interface (CLI) and the Trogon library for terminal user interface (TUI) enhancements, this tool offers a fun and interactive way to play your favorite lotteries.

## Features

- **Interactive CLI**: Generate lottery numbers directly from the command line.
- **TUI Enhancements**: Enjoy an enhanced terminal experience with ASCII art titles for each game.
- **Random Number Generation**: Generates unique random numbers for Eurodreams, Bonoloto, and Euromillones according to official rules.

## Getting Started

### Prerequisites

- Python 3.6+
- Typer library
- Trogon library
- Assets for ASCII art (included in the project)

### Installation

Clone the repository and install the required libraries:

```bash
git clone https://github.com/GeroZayas/Spanish-Lottery-CLI.git
cd Spanish-Lottery-CLI
pip install -r requirements.txt
```


### Usage

Run the application from the command line:
```bash
python3 lottery.py [OPTIONS] COMMAND
```

This will start the CLI where you can select the lottery game you want to play:

- Type `eurodreams` to generate numbers for Eurodreams.
- Type `bonoloto` to generate numbers for Bonoloto.
- Type `euromillones` to generate numbers for Euromillones.

Each command will display the generated numbers in a formatted string, along with an ASCII art title for the game.

## Contributing

Contributions are welcome Feel free to submit a pull request or open an issue to suggest improvements or report bugs.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
