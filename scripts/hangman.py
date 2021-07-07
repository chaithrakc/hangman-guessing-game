import re
import string
from ansi_colors import TerminalColors


class Hangman:
    missed_letters = set()
    char_index_table = dict()

    def __init__(self, word_hint: tuple, hangmans: list, theme: str):
        self.word, self.hint = word_hint
        self.sparse_word = list(string.whitespace[0].join(self.word))
        self.blanks = list(re.sub('\\S+', '_', string.whitespace[0].join(self.word)))
        self.hangmans = hangmans
        self.theme = theme
        self.set_charframe()

    def set_charframe(self):
        for index, char in enumerate(self.sparse_word):
            if char not in string.whitespace[0]:
                self.char_index_table.setdefault(char, list()).append(index)

    def play(self):
        chance = 0
        while chance < len(self.hangmans)-1:
            self.display_hangman(self.hangmans[chance])
            guess = input('Guess the letter or the entire word:')
            if guess == self.word:  # if user gussed the complete word
                self.blanks = string.whitespace[0].join(self.word)
                self.final_display()
                return True
            if len(guess) == 1:  # if user gussed the a letter
                chance = chance + self.guess_exists(guess)
                # check if all the chars are matched
                if self.sparse_word == self.blanks:
                    self.final_display()
                    return True
        self.display_hangman(self.hangmans[chance])
        return False

    def guess_exists(self, guess_char: str) -> int:
        if guess_char not in self.char_index_table:
            if guess_char not in self.missed_letters:
                self.missed_letters.add(guess_char)
                return 1
            else:
                print(
                    f'{TerminalColors.OKGREEN}{TerminalColors.BOLD}Already guessed that letter. Choose again.{TerminalColors.ENDC}')
                return 0
        for index in self.char_index_table.get(guess_char):
            self.blanks[index] = guess_char
        return 0

    def display_hangman(self, hangman):
        lines = hangman.split('\n')
        lines[1] = lines[1] + '\t\t\t\t(' + self.theme + ')'
        lines[2] = lines[2] + '\t\t\tMissed Letters: ' + ','.join(self.missed_letters)
        lines[3] = lines[3] + '\t\t\tWord: ' + ''.join(self.blanks)
        print('\n'.join(lines))

    def final_display(self):
        lines = list()
        lines.append('-'*50)
        lines.append('\t\t\t(' + self.theme + ')')
        lines.append('\t\tMissed Letters: ' + ','.join(self.missed_letters))
        lines.append('\t\tWord: ' + ''.join(self.blanks))
        print('\n'.join(lines))

    # todo based on the probability of winning/losing, provide the hint for the word
    def winning_probability(self) -> int:
        pass
