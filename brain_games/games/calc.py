from random import randint, choice
from operator import add, sub, mul
from brain_games.games.const import LOWER_BOUND, UPPER_BOUND


GAME_HINT = 'What is the result of the expression?'


def get_random_operator():
    """Get a random operator from '+', '-', '*'"""
    operator = choice(['+', '-', '*'])
    return operator


def get_random_numbers():
    """Get random positive numbers"""
    random_number_1 = randint(LOWER_BOUND, UPPER_BOUND)
    random_number_2 = randint(LOWER_BOUND, UPPER_BOUND)
    return random_number_1, random_number_2


def get_expression_result(a, b, operator):
    """Get the result of the generated expression"""
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return sub(a, b)
    elif operator == '*':
        return mul(a, b)


def play_round():
    """Generate a random arithmetic expression and calculates the result"""
    operator = get_random_operator()
    random_number_1, random_number_2 = get_random_numbers()
    correct_answer = str(get_expression_result(random_number_1, random_number_2,
                                               operator))
    expression = f'{random_number_1} {operator} {random_number_2}'
    return correct_answer, expression
