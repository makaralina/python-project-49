from brain_games import engine


game_hint = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_correct_answer(number):
    correct_answer = 'yes' if is_even(number) else 'no'
    return correct_answer


def play_round(name):
    random_number = engine.get_random_number()
    correct_answer = get_correct_answer(random_number)
    answer = engine.get_answer(random_number)
    result = engine.compare_answers(answer, correct_answer, name)
    return result


def run_even_game():
    name = engine.greet_and_get_name()
    print(game_hint)
    for _ in range(engine.ROUNDS):
        round_result = play_round(name)
        if round_result is False:
            break
    else:
        print(f'Congratulations, {name}!')
