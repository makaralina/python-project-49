from brain_games import engine
from random import choice
from operator import add, sub, mul


GAME_HINT = 'What is the result of the expression?'


def get_random_operator():
    """Get a random operator from '+', '-', '*'"""
    operator = choice(['+', '-', '*'])
    return operator


def get_random_numbers():
    """Get random positive numbers"""
    random_number_1 = engine.get_random_number()
    random_number_2 = engine.get_random_number()
    return random_number_1, random_number_2


def get_expression_result(a, b, operator):
    """Get the result of the generated expression"""
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return sub(a, b)
    elif operator == '*':
        return mul(a, b)


def play_round(name):
    """Generate a random expression, get the user's answer
    and compare it with the correct answer"""
    operator = get_random_operator()
    random_number_1, random_number_2 = get_random_numbers()
    expression = f'{random_number_1} {operator} {random_number_2}'
    correct_answer = str(get_expression_result(random_number_1, random_number_2,
                                               operator))
    answer = engine.get_answer(expression)
    result = engine.compare_answers(answer, correct_answer, name)
    return result


def run_calc_game():
    """Play three rounds of the calculator game,
    if the player's answer is incorrect - end the game early"""
    name = engine.greet_and_get_name()
    print(GAME_HINT)
    for _ in range(engine.ROUNDS):
        round_result = play_round(name)
        if round_result is False:
            break
    else:
        print(f'Congratulations, {name}!')
