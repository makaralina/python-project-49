from prompt import string
from random import randint


ROUNDS = 3
GREETING = 'Welcome to the Brain Games!'
LOWER_BOUND = 1
UPPER_BOUND = 100


def greet_and_get_name():
    """Greets the user and returns his name"""
    print(GREETING)
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_answer(data):
    """Asks the question to the user and returns the answer"""
    print(f'Question: {data}')
    answer = string('Your answer: ')
    return answer


def get_random_number():
    return randint(LOWER_BOUND, UPPER_BOUND)


def compare_answers(player_answer, correct_answer, player_name):
    """Compares the user's answer with the correct answer"""
    if player_answer == correct_answer:
        print('Correct!')
    else:
        print(f"'{player_answer}' is wrong answer ;(.",
              f"Correct answer was '{correct_answer}'.", sep=' ')
        print(f"Let's try again, {player_name}!")
        return False
    return True
