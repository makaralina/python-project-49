#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games import calc


def main():
    """Run the calculator game"""
    start_game(calc)


if __name__ == '__main__':
    main()
