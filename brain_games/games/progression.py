from random import randint


GAME_HINT = 'What number is missing in the progression?'


def get_random_progression():
    """Get a random progression with random length,
    random start and random difference"""
    progression = []
    length = randint(5, 10)
    start = randint(0, 20)
    difference = randint(1, 9)
    finish = start + (length - 1) * difference
    for number in range(start, finish + 1, difference):
        progression.append(number)
    return progression


def get_random_index(progression):
    """Get the random index to hide a number in the progression"""
    length_progression = len(progression) - 1
    random_index = randint(0, length_progression)
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


def play_round():
    """Generate a random progression with a missing value,
    and get this missing value as the correct answer"""
    progression = get_random_progression()
    random_index = get_random_index(progression)
    hidden_number = get_hidden_number(progression, random_index)
    progression_with_gap = get_progression_with_gap(progression, random_index)
    correct_answer = str(hidden_number)
    return correct_answer, progression_with_gap
