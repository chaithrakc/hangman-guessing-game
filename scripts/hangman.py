import re
import string

import aesthetics
from aesthetics import *


class Hangman:
    char_table = dict()

    def __init__(self, word_hint: tuple, hangmans: list):
        self.word, self.hint = word_hint
        self.sparse_word = list(string.whitespace[0].join(self.word))
        aesthetics.blanks = list(re.sub('\\S+', '_', string.whitespace[0].join(self.word)))
        self.hangmans = hangmans
        self.set_charframe()
        self.chance = 0

    def set_charframe(self):
        for index, char in enumerate(self.sparse_word):
            if char not in string.whitespace[0]:
                self.char_table.setdefault(char, list()).append(index)

    def start(self) -> bool:
        while self.chance < len(self.hangmans) - 1:
            display_hangman(self.hangmans[self.chance])
            guess = input('Guess the letter or the entire word:')
            if guess == self.word:  # if user gussed the complete word
                aesthetics.blanks = string.whitespace[0].join(self.word)
                return True
            if len(guess) == 1:  # if user gussed a letter
                self.chance = self.chance + self.guess_exists(guess)
                if self.sparse_word == aesthetics.blanks:  # check if all the chars are matched
                    return True
        return False

    def guess_exists(self, guess_char: str) -> int:
        if guess_char not in self.char_table:
            if guess_char not in missed_letters:
                missed_letters.add(guess_char)
                return 1
            print(already_exists)
            return 0
        for index in self.char_table.get(guess_char):
            aesthetics.blanks[index] = guess_char
        return 0

    def play(self):
        result = self.start()
        display_hangman(self.hangmans[self.chance])
        display_results(result, self.word)

    # todo based on the probability of winning/losing, provide the hint for the word
    def winning_probability(self) -> int:
        pass
