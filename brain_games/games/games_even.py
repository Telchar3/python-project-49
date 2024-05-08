#!/usr/bin/env python3
import prompt


def even_number(name):
    from random import randint
    random_number = randint(1, 100)
    print(f'Question: {random_number}')
    answer = prompt.string('Your answer: ')
    if random_number % 2 == 0 and answer.lower() == 'yes' \
            or random_number % 2 == 1 and answer.lower() == 'no':
        print('Correct!')
    elif random_number % 2 == 0:
        print(f"{answer} is wrong answer ;(. Correct answer was 'yes'")
        print(f"Let's try again, {name}")
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was 'no'")
        print(f"Let's try again, {name}")
