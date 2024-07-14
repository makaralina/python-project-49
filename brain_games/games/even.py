from random import randint
from brain_games.const import LOWER_BOUND, UPPER_BOUND


GAME_HINT = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0


def play_round():
    """Generate a random number and get the answer to the question
    'Is it an even number?'"""
    random_number = randint(LOWER_BOUND, UPPER_BOUND)
    correct_answer = 'yes' if is_even(random_number) else 'no'
    return correct_answer, str(random_number)
