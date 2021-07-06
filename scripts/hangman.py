import re


# todo - check for words with spaces from input
class Hangman:
    def __init__(self, word_hint: tuple, hangmans: list, theme: str):
        self.word, self.hint = word_hint
        self.theme = theme
        self.sparse_word = list(' '.join(self.word))
        self.blanks = list(re.sub('\\S+', '_', ' '.join(self.word)))
        self.hangmans = hangmans
        self.missed_letters = set()
        self.char_frame = dict()
        for index, char in enumerate(self.sparse_word):
            if char != ' ':
                self.char_frame.setdefault(char, list()).append(index)

    def play(self):
        for chance in range(len(self.hangmans)):
            self.display_hangman(self.hangmans[chance])
            guess = input('Guess the letter or the entire word:')
            self.match_the_guess(guess)

    def match_the_guess(self, guess: str) -> bool:
        char_indices = self.char_frame.get(guess)
        for index in char_indices:
            self.blanks[index] = guess
        return True

    def display_hangman(self, hangman):
        lines = hangman.split('\n')
        lines[2] = lines[2] + '\t\t\t\t\t(' + self.theme + ')'
        lines[3] = lines[3] + '\t\t\tMissed Letters: ' + ','.join(self.missed_letters)
        lines[4] = lines[4] + '\t\t\tWord: ' + str(self.blanks)
        print('\n'.join(lines))

    # based on the probability of winning/losing, provide the hint for the word
    def winning_probability(self) -> int:
        pass
