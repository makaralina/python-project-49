from brain_games import engine


game_hint = 'What number is missing in the progression?'


def get_random_length():
    """Get the random length of the progression"""
    random_length = engine.get_random_number(LOWER_BOUND=5, UPPER_BOUND=10)
    return random_length


def get_random_start():
    """Get the random start of the progression"""
    random_start = engine.get_random_number(LOWER_BOUND=0, UPPER_BOUND=20)
    return random_start


def get_random_difference():
    """Get the random progression difference"""
    random_difference = engine.get_random_number(LOWER_BOUND=1, UPPER_BOUND=9)
    return random_difference


def get_random_progression():
    """Get a random progression with a given length"""
    progression = []
    length = get_random_length()
    start = get_random_start()
    next_number = start
    difference = get_random_difference()
    for _ in range(length):
        if len(progression) == 0:
            progression.append(start)
        else:
            next_number += difference
            progression.append(next_number)
    return progression


def get_random_index(progression):
    """Get the random index to hide a number in the progression"""
    length_progression = len(progression) - 1
    random_index = engine.get_random_number(LOWER_BOUND=0,
                                            UPPER_BOUND=length_progression)
    return random_index


def get_hidden_number(progression, random_index):
    """Get the hidden number by index"""
    hidden_number = progression[random_index]
    return hidden_number


def get_progression_with_gap(progression, random_index):
    """Get the progression with a missing value"""
    progression[random_index] = ".."
    progression_with_gap = ' '.join(str(value) for value in progression)
    return progression_with_gap


def play_round(name):
    """Generate a random progression with a missing value,
    get the user's answer and compare it with the correct answer"""
    progression = get_random_progression()
    random_index = get_random_index(progression)
    hidden_number = get_hidden_number(progression, random_index)
    progression_with_gap = get_progression_with_gap(progression, random_index)
    correct_answer = str(hidden_number)
    answer = engine.get_answer(progression_with_gap)
    result = engine.compare_answers(answer, correct_answer, name)
    return result


def run_progression_game():
    """Play three rounds of the game to guess the hidden number
    in the progression, if the player's answer is incorrect
    - end the game early"""
    name = engine.greet_and_get_name()
    print(game_hint)
    for _ in range(engine.ROUNDS):
        round_result = play_round(name)
        if round_result is False:
            break
    else:
        print(f'Congratulations, {name}!')
