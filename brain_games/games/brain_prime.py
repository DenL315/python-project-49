import random
import math
QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_task():
    num = random.randint(0, 100)
    question = num
    if is_prime(num) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def is_prime(num)
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0 or num == 0 or num == 1:
            return False
        i += 1
    return True
