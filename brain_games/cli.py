from prompt import string


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
