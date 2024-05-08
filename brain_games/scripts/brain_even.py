#!/usr/bin/env python3
import prompt
tried = 0


def even_number(name):
    from random import randint
    global tried
    random_number = randint(1, 100)
    print(f'Question: {random_number}')
    answer = prompt.string('Your answer: ')
    if random_number % 2 == 0 and answer.lower() == 'yes' \
            or random_number % 2 == 1 and answer.lower() == 'no':
        print('Correct!')
        tried = tried + 1
    elif random_number % 2 == 0:
        print(f"{answer} is wrong answer ;(. Correct answer was 'yes'")
        print(f"Let's try again, {name}!")
        tried = 100
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was 'no'")
        print(f"Let's try again, {name}!")
        tried = 100


def main():
    print('Welcome to the Brain Games')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while tried < 3:
        even_number(name)
        if tried == 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
