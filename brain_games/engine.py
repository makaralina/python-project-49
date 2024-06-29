from prompt import string


ROUNDS = 3


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    greet()
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_answer(data):
    print(f'Question: {data}')
    answer = string('Your answer: ')
    return answer


def compare_answers(player_answer, correct_answer, player_name):
    if player_answer == correct_answer:
        print('Correct!')
    else:
        print(f"'{player_answer}' is wrong answer ;(.",
              f"Correct answer was '{correct_answer}'.", sep=' ')
        print(f"Let's try again, {player_name}!")
        return False
