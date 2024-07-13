#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games import gcd


def main():
    """Run the game of finding the greatest common divisor for two numbers"""
    start_game(gcd)


if __name__ == '__main__':
    main()
