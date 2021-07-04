import json
import os
import random

from hangman import Hangman


def load_word_theme() -> dict:
    resources = os.listdir('../resources')
    theme_files = list(filter(lambda input_file: input_file.startswith('word_theme_'), resources))
    random_theme = random.choice(theme_files)
    relative_filepath = os.path.join('', '../resources', '../resources/'+random_theme)
    with open(relative_filepath) as file_handler:
        return json.load(file_handler)


def load_hangman_pics() -> list:
    relative_filepath = os.path.join('', '../resources', 'hangman_pics.txt')
    with open(relative_filepath) as file_handler:
        hangmans_pics = file_handler.read()
        return hangmans_pics.split(',')


if __name__ == '__main__':
    hangmans = load_hangman_pics()
    theme = load_word_theme()
    word_hint = random.choice(list(theme.items()))
    hangman = Hangman(word_hint, hangmans)
    hangman.play()
