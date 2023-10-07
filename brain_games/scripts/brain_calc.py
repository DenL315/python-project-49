#!/usr/bin/env python3

def brain_calc():
    import prompt, random
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    counter = 0
    calc_list = ['+', '-','*']
    while counter < 3:
        a, b = random.randint(0, 100), random.randint(0, 100)
        c = random.choice(calc_list)
        if c == '+':
            correct_answer = str(a + b)
        elif c == '-':
            correct_answer = str(a - b)
        else:
            correct_answer = str(a * b)
        test1 = prompt.string(f'Question: {a} {c} {b}\nYour answer: ')
        if test1 == correct_answer:
            print('Correct!')
            counter += 1
            if counter == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{test1}' is wrong answer ;(. Correct answer is '{correct_answer}'.\nLet's try again, {name}!")
            break

def main():
    brain_calc()


if __name__ == '__main__':
    main()