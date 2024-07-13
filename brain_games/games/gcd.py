from brain_games import engine


game_hint = 'Find the greatest common divisor of given numbers.'


def get_random_numbers():
    """Get two random numbers"""
    random_number_1 = engine.get_random_number()
    random_number_2 = engine.get_random_number()
    return random_number_1, random_number_2


def find_gcd(a, b):
    """Find the greatest common divisor of given numbers"""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def play_round(name):
    """Generate a pair of random numbers to calculate 'gcd',
    get the user's answer and compare it with the correct answer"""
    a, b = get_random_numbers()
    expression = f'{a} {b}'
    correct_answer = str(find_gcd(a, b))
    answer = engine.get_answer(expression)
    result = engine.compare_answers(answer, correct_answer, name)
    return result


def run_gcd_game():
    """Play three rounds of the game to find the greatest common
    divisor of two numbers, if the player's answer is incorrect
    - end the game early"""
    name = engine.greet_and_get_name()
    print(game_hint)
    for _ in range(engine.ROUNDS):
        round_result = play_round(name)
        if round_result is False:
            break
    else:
        print(f'Congratulations, {name}!')
