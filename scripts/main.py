import os
import random

from hangman import Hangman


def load_word_theme():
    relative_filepath = os.path.join('', '../resources', 'word_theme_animal.txt')
    with open(relative_filepath) as file_handler:
        banner_str = file_handler.read()
        return banner_str.split(',')


if __name__ == '__main__':
    words = load_word_theme()
    hangman = Hangman(random.choice(words))
    hangman.load_hangman_pics()
    hangman.play()
