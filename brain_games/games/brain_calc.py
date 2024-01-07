import random
import operators

QUESTION = 'What is the result of the expression?'


def generate_task():
    calc_list = ['+', '-', '*']
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    operator = random.choice(calc_list)
    question = f'{num1} {operator} {num2}'
    correct_answer = str(operator_return(operator))
    return question, correct_answer


def operator_return(operator):
    if operator == '+':
        return operators.add(num1, num2)
    elif operator == '-':
        return operators.sub(num1, num2)
    else:
        return operators.mul(num1, num2)
