from random import randint, choice
from operator import add, sub, mul
from brain_games.const import LOWER_BOUND, UPPER_BOUND


GAME_HINT = 'What is the result of the expression?'


def get_random_operator():
    """Get a random operator from '+', '-', '*'"""
    operator = choice(['+', '-', '*'])
    return operator


def get_random_numbers():
    """Get two random numbers"""
    random_number_1 = randint(LOWER_BOUND, UPPER_BOUND)
    random_number_2 = randint(LOWER_BOUND, UPPER_BOUND)
    return random_number_1, random_number_2


def get_expression_result(a, b, operator):
    """Get the result of the generated expression"""
    match operator:
        case '+':
            return add(a, b)
        case '-':
            return sub(a, b)
        case '*':
            return mul(a, b)


def play_round():
    """Generate a random arithmetic expression and calculates its result"""
    operator = get_random_operator()
    number_1, number_2 = get_random_numbers()
    correct_answer = str(get_expression_result(number_1, number_2, operator))
    expression = f'{number_1} {operator} {number_2}'
    return correct_answer, expression
