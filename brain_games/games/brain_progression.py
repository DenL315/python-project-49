import random
QUESTION = 'What number is missing in the progression?'


def generate_task():
    begin = random.randint(0, 10)
    step = random.randint(3, 6)
    end = random.randint(50, 70)
    progression = list(range(begin, end, step))
    index = random.randint(0, len(progression) - 1)
    correct_answer = str(progression[index])
    progression[index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
