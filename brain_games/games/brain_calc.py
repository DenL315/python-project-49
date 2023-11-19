import random

QUESTION = 'What is the result of the expression?'


def generate_task():
    calc_list = ['+', '-', '*']
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    operator = random.choice(calc_list)
    question = f'{num1} {operator} {num2}'
    if operator == '+':
        correct_answer = str(num1 + num2)
    elif operator == '-':
        correct_answer = str(num1 - num2)
    else:
        correct_answer = str(num1 * num2)
    return question, correct_answer
