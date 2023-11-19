import random
import math
QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_task():
    num = random.randint(0, 100)
    i = 2
    question = num
    correct_answer = 'yes'
    while i <= math.sqrt(num):
        if num % i == 0 or num == 0 or num == 1:
            correct_answer = 'no'
        i += 1
    return question, correct_answer
