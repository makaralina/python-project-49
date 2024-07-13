from random import randint
from brain_games.games.const import LOWER_BOUND, UPPER_BOUND


GAME_HINT = 'Find the greatest common divisor of given numbers.'


def get_random_numbers():
    """Get two random numbers"""
    random_number_1 = randint(LOWER_BOUND, UPPER_BOUND)
    random_number_2 = randint(LOWER_BOUND, UPPER_BOUND)
    return random_number_1, random_number_2


def find_gcd(a, b):
    """Find the greatest common divisor of given numbers"""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def play_round():
    """Generate a pair of random numbers to calculate 'gcd',
    get the user's answer and compare it with the correct answer"""
    a, b = get_random_numbers()
    expression = f'{a} {b}'
    correct_answer = str(find_gcd(a, b))
    return correct_answer, expression
