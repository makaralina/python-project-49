from brain_games import engine
from random import choice


game_hint = 'What is the result of the expression?'


def get_random_expression():
    """Get a random expression, for example '6 * 3' or '5 + 6'"""
    random_number_1 = engine.get_random_number()
    random_number_2 = engine.get_random_number()
    operator = choice(['+', '-', '*'])
    expression = f'{random_number_1} {operator} {random_number_2}'
    return expression


def play_round(name):
    """Generate a random expression, get the user's answer
    and compare it with the correct answer"""
    expression = get_random_expression()
    correct_answer = str(eval(expression))
    answer = engine.get_answer(expression)
    result = engine.compare_answers(answer, correct_answer, name)
    return result


def run_calc_game():
    """Play three rounds of the calculator game,
    if the player's answer is incorrect - end the game early"""
    name = engine.greet_and_get_name()
    print(game_hint)
    for _ in range(engine.ROUNDS):
        round_result = play_round(name)
        if round_result is False:
            break
    else:
        print(f'Congratulations, {name}!')
