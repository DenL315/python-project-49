import random
import operator

QUESTION = 'What is the result of the expression?'


def generate_task():
    calc_list = ['+', '-', '*']
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    random_operator = random.choice(calc_list)
    question = f'{num1} {random_operator} {num2}'
    correct_answer = str(operator_return(random_operator, num1, num2))
    return question, correct_answer


def operator_return(random_operator, num1, num2):
    if random_operator == '+':
        return operator.add(num1, num2)
    elif random_operator == '-':
        return operator.sub(num1, num2)
    else:
        return operator.mul(num1, num2)
