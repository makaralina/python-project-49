from prompt import string


ROUNDS = 3
GREETING = 'Welcome to the Brain Games!'


def greet_and_get_name():
    """Greet the user and return his name"""
    print(GREETING)
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_user_answer(question):
    """Ask the question to the user and return his answer"""
    print(f'Question: {str(question)}')
    answer = string('Your answer: ')
    return answer


def compare_answers(player_answer, correct_answer, player_name):
    """Compare the player's answer with the correct answer"""
    if player_answer == correct_answer:
        print('Correct!')
    else:
        print(f"'{player_answer}' is wrong answer ;(.",
              f"Correct answer was '{correct_answer}'.", sep=' ')
        print(f"Let's try again, {player_name}!")
        return False
    return True


def start_game(game):
    """Play three rounds of the game, if the player's
    answer is incorrect - end the game early"""
    name = greet_and_get_name()
    print(game.GAME_HINT)
    for _ in range(ROUNDS):
        correct_answer, question = game.play_round()
        user_answer = get_user_answer(question)
        result = compare_answers(user_answer, correct_answer, name)
        if result is False:
            break
    else:
        print(f'Congratulations, {name}!')
