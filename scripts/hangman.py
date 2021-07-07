import re
import string

from display import *


class Hangman:
    char_table = dict()

    def __init__(self, secret_word: str, hangmans: list):
        self.word = secret_word
        self.sparse_word = list(' '.join(self.word))
        self.blanks = list(re.sub('\\S+', '_', ' '.join(self.word)))
        self.hangmans = hangmans
        self.set_charframe()
        self.missed_letters = set()

    def set_charframe(self):
        for index, char in enumerate(self.sparse_word):
            if char not in string.whitespace[0]:
                self.char_table.setdefault(char, list()).append(index)

    def start(self) -> bool:
        while len(self.missed_letters) < len(self.hangmans) - 1:
            display_hangman(self.winning_probability(), self.hangmans, self.missed_letters, self.blanks)
            guess = input('Guess the letter or the entire word:')
            if guess == self.word:  # if user gussed the complete word
                self.blanks = ' '.join(self.word)
                return True
            if len(guess) == 1:  # if user gussed a letter
                self.guess_exists(guess)
                if self.sparse_word == self.blanks:  # check if all the chars are matched
                    return True
        return False

    def guess_exists(self, guess_char: str) -> int:
        if guess_char not in self.char_table:
            if guess_char not in self.missed_letters:
                self.missed_letters.add(guess_char)
                return 1
            print(already_exists)
            return 0
        for index in self.char_table.get(guess_char):
            self.blanks[index] = guess_char
        return 0

    def play(self):
        result = self.start()
        display_hangman(self.winning_probability(), self.hangmans, self.missed_letters, self.blanks)
        display_results(result, self.word)

    def winning_probability(self) -> int:
        num_blanks = list(filter(lambda char: char == '_', self.blanks))
        return len(self.hangmans) - len(num_blanks)
