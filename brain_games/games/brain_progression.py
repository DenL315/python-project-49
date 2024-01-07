import random
QUESTION = 'What number is missing in the progression?'


def generate_task():
    progression = create_progression()
    index = random.randint(0, len(progression) - 1)
    correct_answer = str(progression[index])
    progression[index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer


def create_progression():
    begin = random.randint(0, 10)
    step = random.randint(3, 6)
    end = random.randint(50, 70)
    return list(range(begin, end, step))
