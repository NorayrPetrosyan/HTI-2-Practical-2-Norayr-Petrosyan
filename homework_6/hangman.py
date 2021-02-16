import random
import os

def get_a_random_word():
    file_name = 'fruits.txt'
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, file_name)

    with open('fruits.txt') as fruit:
        fruits = [row for row in fruit.readlines()]
        return random.choice(fruits)


def guess_output(guess):
    for j in range(len(guess)):
        print(guess[j], end=' ')

def hangman(word, guess, mistakes):

    if mistakes == 0 and '_' in guess:
        return 'You lost the game.'
    if mistakes > 0 and "_" not in guess:
        guess_output(guess)
        print()
        return 'You won the game.'

    print(f'Guess the word. {mistakes} mistakes left.')

    guess_output(guess)
    print()

    letter = input("Guess a letter: ").upper()

    for i in range(len(word)):
        if word[i].upper() == letter:
            guess[i] = letter

    if not letter in word.upper():
        mistakes = mistakes - 1

    return hangman(word, guess, mistakes)


fruit_name = get_a_random_word().split('\n')[0]
print(hangman(fruit_name, guess = ("_ " * len(fruit_name)).split(), mistakes=5))