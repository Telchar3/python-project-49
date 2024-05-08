#!usr/bin/env python3
import prompt
tried = 0


def brain_gcd(name):
    from random import randint
    global tried
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
        tried = tried + 1
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'")
        print(f"Let's try again, {name}!")
        tried = 100


def main():
    print('Welcome to the Brain Games')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Find the greatest common divisor of given numbers.')
    while tried < 3:
        brain_gcd(name)
        if tried == 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
