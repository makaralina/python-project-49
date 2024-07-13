from brain_games import engine


game_hint = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0


def get_correct_answer(number):
    """Return 'yes' if the number is even, otherwise answer 'no'"""
    correct_answer = 'yes' if is_even(number) else 'no'
    return correct_answer


def play_round(name):
    """Generate a random number, get the user's answer to the question
    'Is it an even number?' and compare it with the correct answer"""
    random_number = engine.get_random_number()
    correct_answer = get_correct_answer(random_number)
    answer = engine.get_answer(random_number)
    result = engine.compare_answers(answer, correct_answer, name)
    return result


def run_even_game():
    """Play three rounds of the parity check game,
    if the player's answer is incorrect - end the game early"""
    name = engine.greet_and_get_name()
    print(game_hint)
    for _ in range(engine.ROUNDS):
        round_result = play_round(name)
        if round_result is False:
            break
    else:
        print(f'Congratulations, {name}!')
