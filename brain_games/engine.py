from prompt import string
from random import randint


ROUNDS = 3
GREETING = 'Welcome to the Brain Games!'
LOWER_BOUND = 1
UPPER_BOUND = 10


def greet_and_get_name():
    """Greet the user and return his name"""
    print(GREETING)
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_answer(data):
    """Ask the question to the user and return his answer"""
    print(f'Question: {str(data)}')
    answer = string('Your answer: ')
    return answer


def get_random_number():
    """Generate a random number"""
    return randint(LOWER_BOUND, UPPER_BOUND)


def compare_answers(player_answer, correct_answer, player_name):
    """Compare the user's answer with the correct answer"""
    if player_answer == correct_answer:
        print('Correct!')
    else:
        print(f"'{player_answer}' is wrong answer ;(.",
              f"Correct answer was '{correct_answer}'.", sep=' ')
        print(f"Let's try again, {player_name}!")
        return False
    return True
