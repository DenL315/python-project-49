#!/usr/bin/env python3
import prompt, random


def brain_progression():
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    counter = 0
    while counter < 3:
        a, b = random.randint(0, 10), random.randint(3, 6)
        d = random.randint(50, 70)
        progression = list(range(a, d, b))
        c = random.randint(0,len(progression) - 1)
        correct_answer = str(progression[c])
        progression[c] = '..'
        proverka = ' '.join(map(str, progression))
        test1 = prompt.string(f'Question: {proverka}\nYour answer: ')
        if test1 == correct_answer:
            print('Correct!')
            counter += 1
            if counter == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{test1}' is wrong answer ;(. Correct answer is '{correct_answer}'.\nLet's try again, {name}!")
            break


def main():
    brain_progression()


if __name__ == '__main__':
    main()
