import json
import os
import random

from hangman import Hangman


class Game:

    def __init__(self):
        self.themes = ['Animal', 'Movie', 'Place']
        self.theme = None

    def load_word_theme(self) -> dict:
        resources = os.listdir('../resources')
        self.theme = random.choice(self.themes).lower()
        file_name = list(filter(lambda input_file: input_file.find(self.theme) > -1, resources))
        relative_filepath = os.path.join('', '../resources', '../resources/' + file_name[0])
        with open(relative_filepath) as file_handler:
            return json.load(file_handler)

    def load_hangman_pics(self) -> list:
        relative_filepath = os.path.join('', '../resources', 'hangman_pics.txt')
        with open(relative_filepath) as file_handler:
            hangmans_pics = file_handler.read()
            return hangmans_pics.split(',')


if __name__ == '__main__':
    game = Game()
    hangmans = game.load_hangman_pics()
    words = game.load_word_theme()
    word_hint = random.choice(list(words.items()))
    hangman = Hangman(word_hint, hangmans, game.theme)
    hangman.play()
