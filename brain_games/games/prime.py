from random import randint
from brain_games.games.const import LOWER_BOUND, UPPER_BOUND


GAME_HINT = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number(number):
    """Check if a number is prime"""
    if number <= 1:
        return False
    divider = 2
    while divider <= number ** 0.5:
        if number % divider == 0:
            return False
        divider += 1
    return True


def get_correct_answer(number):
    """Return 'yes' if the number is prime, otherwise answer 'no'"""
    correct_answer = 'yes' if is_prime_number(number) else 'no'
    return correct_answer


def play_round():
    """Generate a random number, get the user's answer to the question
    'Is it a prime number?' and compare it with the correct answer"""
    random_number = randint(LOWER_BOUND, UPPER_BOUND)
    correct_answer = get_correct_answer(random_number)
    return correct_answer, str(random_number)
