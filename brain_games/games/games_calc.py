#!/usr/bin/env python3
def brain_calc(name):
    import prompt
    from random import randint, choice
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
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
        print(f"Let's try again, {name}!")
