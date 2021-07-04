import os


class Hangman:
    handman_pics = None

    def __init__(self, input_word):
        self.input_word = input_word

    def load_hangman_pics(self) -> None:
        relative_filepath = os.path.join('', '../resources', 'hangman_pics.txt')
        with open(relative_filepath) as file_handler:
            hangmans = file_handler.read()
            print(hangmans)

    def play(self):
        print(self.input_word)