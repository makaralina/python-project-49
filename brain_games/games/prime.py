from random import randint
from brain_games.const import LOWER_BOUND, UPPER_BOUND


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


def play_round():
    """Generate a random number and get the answer to the question
    'Is it a prime number?'"""
    random_number = randint(LOWER_BOUND, UPPER_BOUND)
    correct_answer = 'yes' if is_prime_number(random_number) else 'no'
    return correct_answer, str(random_number)
