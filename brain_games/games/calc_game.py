from brain_games import engine
from random import choice


game_hint = 'What is the result of the expression?'


def get_random_expression():
    random_number_1 = engine.get_random_number()
    random_number_2 = engine.get_random_number()
    operator = choice(['+', '-', '*'])
    expression = f'{random_number_1} {operator} {random_number_2}'
    return expression


def play_round(name):
    expression = get_random_expression()
    correct_answer = str(eval(expression))
    answer = engine.get_answer(expression)
    result = engine.compare_answers(answer, correct_answer, name)
    return result


def run_calc_game():
    name = engine.greet_and_get_name()
    print(game_hint)
    for _ in range(engine.ROUNDS):
        round_result = play_round(name)
        if round_result is False:
            break
    else:
        print(f'Congratulations, {name}!')
