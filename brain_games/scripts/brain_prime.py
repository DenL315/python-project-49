#!/usr/bin/env python3

def brain_prime():
    import prompt, random, math
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0
    while counter < 3:
        a = random.randint(0, 100)
        i = 2
        correct_answer = 'yes'
        while i <= math.sqrt(a):
            if a % i == 0:
                correct_answer = 'no'
            i += 1
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
    brain_prime()


if __name__ == '__main__':
    main()
