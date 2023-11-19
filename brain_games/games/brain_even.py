import random
QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_task():
    num = random.randint(0, 100)
    question = num
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
