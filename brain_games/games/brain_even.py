#!/usr/bin/env python3
import prompt, random


def brain_even():
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        a = random.randint(0, 100)
        if a % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        test1 = prompt.string(f'Question: {a}\nYour answer: ')
        if test1 == correct_answer:
            print('Correct!')
            counter += 1
            if counter == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{test1}' is wrong answer ;(. Correct answer is '{correct_answer}'.\nLet's try again, {name}!")
            break


def main():
    brain_even()


if __name__ == '__main__':
    main()