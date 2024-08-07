#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games import prime


def main():
    """Run the game to check if the number is prime"""
    start_game(prime)


if __name__ == '__main__':
    main()
