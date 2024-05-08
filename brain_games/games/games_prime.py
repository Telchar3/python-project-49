#!usr/bin/env python3
import prompt


def brain_prime(name):
    from random import randint
    result = 'yes'
    rand_number = randint(1, 101)
    half_rand_number = rand_number // 2
    if rand_number == 1:
        result = 'no'
    for i in range(2, half_rand_number + 1):
        if rand_number % i == 0:
            result = 'no'
    print(f'Question: {rand_number}')
    answer = prompt.string('Your answer: ')
    if answer.lower() == result:
        print('Correct!')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'")
        print(f"Let's try again, {name}!")
