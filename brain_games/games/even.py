from random import randint
from brain_games.games.const import LOWER_BOUND, UPPER_BOUND


GAME_HINT = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0


def get_correct_answer(number):
    """Return 'yes' if the number is even, otherwise answer 'no'"""
    correct_answer = 'yes' if is_even(number) else 'no'
    return correct_answer


def play_round():
    """Generate a random number, get the user's answer to the question
    'Is it an even number?' and compare it with the correct answer"""
    random_number = randint(LOWER_BOUND, UPPER_BOUND)
    correct_answer = get_correct_answer(random_number)
    return correct_answer, str(random_number)
