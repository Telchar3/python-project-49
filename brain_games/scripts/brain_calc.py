#!/usr/bin/env python3
import prompt
tried = 0


def brain_calc(name):
    from random import randint, choice
    global tried
    random_number_one = randint(1, 100)
    random_number_two = randint(1, 100)
    result = 0
    operation = choice(['+', '-', '*'])
    if operation == '+':
        result = random_number_one + random_number_two
    elif operation == '-':
        result = random_number_one - random_number_two
    elif operation == '*':
        result = random_number_one * random_number_two
    print(f'Question: {random_number_one} {operation} {random_number_two}')
    answer = prompt.string('Your answer: ')
    if answer == str(result):
        print('Correct!')
        tried = tried + 1
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
        print(f"Let's try again, {name}!")
        tried = 100


def main():
    print('Welcome to the Brain Games')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What is the result on the expression?')
    while tried < 3:
        brain_calc(name)
        if tried == 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
