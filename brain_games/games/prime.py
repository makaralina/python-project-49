from brain_games import engine


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


def get_correct_answer(number):
    """Return 'yes' if the number is prime, otherwise answer 'no'"""
    correct_answer = 'yes' if is_prime_number(number) else 'no'
    return correct_answer


def play_round(name):
    """Generate a random number, get the user's answer to the question
    'Is it a prime number?' and compare it with the correct answer"""
    random_number = engine.get_random_number()
    correct_answer = get_correct_answer(random_number)
    answer = engine.get_answer(random_number)
    result = engine.compare_answers(answer, correct_answer, name)
    return result


def run_prime_game():
    """Play three rounds to check if the number is prime,
    if the player's answer is incorrect - end the game early"""
    name = engine.greet_and_get_name()
    print(GAME_HINT)
    for _ in range(engine.ROUNDS):
        round_result = play_round(name)
        if round_result is False:
            break
    else:
        print(f'Congratulations, {name}!')
