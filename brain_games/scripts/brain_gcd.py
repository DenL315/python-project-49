#!/usr/bin/env python3

def brain_gcd():
    import prompt, random, math
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    counter = 0
    while counter < 3:
        a, b = random.randint(0, 100), random.randint(0, 100)
        correct_answer = str(math.gcd(a, b))
        test1 = prompt.string(f'Question: {a} {b}\nYour answer: ')
        if test1 == correct_answer:
            print('Correct!')
            counter += 1
            if counter == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{test1}' is wrong answer ;(. Correct answer is '{correct_answer}'.\nLet's try again, {name}!")
            break

def main():
    brain_gcd()


if __name__ == '__main__':
    main()