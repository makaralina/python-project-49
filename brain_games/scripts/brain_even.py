#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games import even


def main():
    """Run the parity check game"""
    start_game(even)


if __name__ == '__main__':
    main()
