from random import randint
from brain_games import engine


def run_even_game():
    name = engine.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(engine.ROUNDS):
        random_number = randint(1, 100)
        correct_answer = 'yes' if random_number % 2 == 0 else 'no'
        answer = engine.get_answer(random_number)
        result = engine.compare_answers(answer, correct_answer, name)
        if result is False:
            break
    else:
        print(f'Congratulations, {name}!')
