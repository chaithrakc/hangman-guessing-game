import json
import os
import random

from hangman import Hangman


class App:
    word_them = None
    WORD_THEME_ = 'word_theme_'

    def set_theme(self, file_name: str):
        start_index = file_name.index(self.WORD_THEME_) + len(self.WORD_THEME_)
        end_index = file_name.index('.json')
        self.word_them = file_name[start_index: end_index]

    def load_word_theme(self) -> dict:
        resources = os.listdir('../resources')
        word_files = list(filter(lambda input_file: input_file.find(self.WORD_THEME_) > -1, resources))
        file_name = random.choice(word_files)  # randomly selecting one of the theme
        self.set_theme(file_name)
        relative_filepath = os.path.join('', '../resources', '../resources/' + file_name)
        with open(relative_filepath) as file_handler:
            return json.load(file_handler)

    def load_hangman_pics(self) -> list:
        relative_filepath = os.path.join('', '../resources', 'hangman_pics.txt')
        with open(relative_filepath) as file_handler:
            hangmans_pics = file_handler.read()
            return hangmans_pics.split(',')


if __name__ == '__main__':
    app = App()
    hangmans = app.load_hangman_pics()
    words = app.load_word_theme()
    word_hint = random.choice(list(words.items()))  # randomly selecting a word withing a particular theme file
    hangman = Hangman(word_hint, hangmans, app.word_them)
    won = hangman.play()
    print('You Won!' if won else 'You Lost.')
