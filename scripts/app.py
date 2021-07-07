import json
import os
import random

from ansi_colors import TerminalColors
from hangman import Hangman


class App:
    word_them = None
    WORD_THEME_ = 'word_theme_'

    def set_theme(self, file_name: str):
        self.word_them = file_name[file_name.index(self.WORD_THEME_) + len(self.WORD_THEME_): file_name.index('.json')]

    def load_word_theme(self) -> dict:
        resources = os.listdir(os.path.join('..', 'resources'))
        word_files = list(filter(lambda input_file: input_file.find(self.WORD_THEME_) > -1, resources))
        file_name = random.choice(word_files)  # randomly selecting one of the theme
        self.set_theme(file_name)
        relative_filepath = os.path.join('..', 'resources', file_name)
        with open(relative_filepath) as file_handler:
            return json.load(file_handler)

    def load_hangman_pics(self) -> list:
        relative_filepath = os.path.join('..', 'resources', 'hangman_pics.txt')
        with open(relative_filepath) as file_handler:
            hangmans_pics = file_handler.read()
            return hangmans_pics.split(',')

    def display_results(self, results):
        print('-' * 50)
        won = f'\t\t\t{TerminalColors.FAIL}YOU WON!{TerminalColors.ENDC}'
        lost = f'\t\t\t{TerminalColors.FAIL}YOU LOST{TerminalColors.ENDC}'
        print(won if results else lost)
        print(f'\tSecret Word is {TerminalColors.FAIL}{word_hint[0]}!{TerminalColors.ENDC}')
        print('-' * 50)


if __name__ == '__main__':
    app = App()
    hangmans = app.load_hangman_pics()
    words = app.load_word_theme()
    word_hint = random.choice(list(words.items()))  # randomly selecting a word withing a particular theme file
    hangman = Hangman(word_hint, hangmans, app.word_them)
    result = hangman.play()
    app.display_results(result)
