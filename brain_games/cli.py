def welcome_user():
    import prompt
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!')


def main():
    welcome_user()
