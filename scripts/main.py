import json
import os
import random

from hangman import Hangman


def load_word_theme() -> dict:
    relative_filepath = os.path.join('', '../resources', '../resources/word_theme_animal.json')
    with open(relative_filepath) as file_handler:
        return json.load(file_handler)


def load_hangman_pics() -> list:
    relative_filepath = os.path.join('', '../resources', 'hangman_pics.txt')
    with open(relative_filepath) as file_handler:
        hangmans_pics = file_handler.read()
        hangmans_pics = hangmans_pics.split(',')
        return hangmans_pics


if __name__ == '__main__':
    words = load_word_theme()
    hangmans = load_hangman_pics()
    hangman = Hangman(words, hangmans)
    hangman.play()
