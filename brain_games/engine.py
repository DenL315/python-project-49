import prompt
ROUND_TO_WIN = 3


def play(game):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!')
    print(game.QUESTION)
    for _ in range(ROUND_TO_WIN):
        question, correct_answer = game.generate_task()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. ,"
                  f"Correct answer is '{correct_answer}'.,"
                  f"\nLet's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
