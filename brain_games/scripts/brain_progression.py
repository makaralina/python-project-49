#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games import progression


def main():
    """Run the parity check game"""
    start_game(progression)


if __name__ == '__main__':
    main()
