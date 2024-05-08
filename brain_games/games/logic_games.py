#!usr/bin/env python3
import prompt
tried = 0


def logic(name):
    global tried
    result = 0
    print('Question: ')
    answer = prompt.string('Your answer: ')
    if answer == result:
        print('Correct!')
        tried = tried + 1
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was ' '")
        print(f"Let's try again, {name}")
        tried = 100


def main():
    print('Welcome to the Brain Games')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Question')
    while tried < 3:
        logic(name)
        if tried == 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
