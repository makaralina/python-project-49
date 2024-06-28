from random import randint
from prompt import string
from brain_games import engine


def run_even_game():
    name = engine.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    ROUNDS = 3
    for _ in range(ROUNDS):
        random_number = randint(1, 100)
        correct_answer = 'yes' if random_number % 2 == 0 else 'no'
        print(f'Question: {random_number}')
        answer = string('Your answer: ')
        result = engine.compare_answers(answer, correct_answer, name)
        if result is False:
            break
    else:
        print(f'Congratulations, {name}!')
