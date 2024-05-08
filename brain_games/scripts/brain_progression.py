#!usr/bin/env python3
import prompt
tried = 0


def brain_progression(name):
    from random import randint
    global tried
    rand_step = randint(2, 10)
    begin_number = randint(1, 100)
    result = ''
    our_number = 0
    rand_number = randint(1, 10)
    rand_lengt = randint(5, 10)
    begin_number2 = begin_number + rand_step * rand_number
    step = rand_step * (rand_number - 1)
    for i in range(begin_number, begin_number + step, rand_step):
        result = result + str(i) + ' '
    result = result + '.. '
    our_number = begin_number + step
    for i in range(
        begin_number2,
        begin_number2 + rand_step * ((rand_lengt - rand_number) - 1),
        rand_step
    ):
        result = result + str(i) + ' '
    print(f'Question: {result}')
    answer = prompt.string('Your answer: ')
    if answer == str(our_number):
        print('Correct!')
        tried = tried + 1
    else:
        error_message = (
            f"'{answer}' is wrong answer ;(. "
            f"Correct answer was '{our_number}'"
        )
        print(error_message)
        print(f"Let's try again, {name}!")
        tried = 100


def main():
    print('Welcome to the Brain Games')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What number is missing in the progression?')
    while tried < 3:
        brain_progression(name)
        if tried == 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
