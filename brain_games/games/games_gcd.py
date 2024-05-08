#!usr/bin/env python3
import prompt


def brain_gcd(name):
    from random import randint
    result = 1
    rand_num_one = randint(1, 100)
    rand_num_two = randint(1, 100)
    print(f'Question: {rand_num_one} {rand_num_two}')
    while rand_num_one != rand_num_two:
        if rand_num_one > rand_num_two:
            rand_num_one = rand_num_one - rand_num_two
        else:
            rand_num_two = rand_num_two - rand_num_one
        result = rand_num_one
    answer = prompt.string('Your answer: ')
    if answer == str(result):
        print('Correct!')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'")
        print(f"Let's try again, {name}!")
