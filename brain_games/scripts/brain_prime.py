#!usr/bin/env python3
import prompt
tried = 0


def brain_prime(name):
    from random import randint
    global tried
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
        tried = tried + 1
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'")
        print(f"Let's try again, {name}!")
        tried = 100


def main():
    print('Welcome to the Brain Games')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while tried < 3:
        brain_prime(name)
        if tried == 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
