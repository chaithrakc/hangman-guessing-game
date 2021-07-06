import re


# todo - check for words with spaces from input
class Hangman:
    def __init__(self, word_hint: tuple, hangmans: list, theme: str):
        self.char_frame = dict()
        self.word, self.hint = word_hint
        self.theme = theme
        self.sparse_word = list(' '.join(self.word))
        self.blanks = list(re.sub('\\S+', '_', ' '.join(self.word)))
        self.hangmans = hangmans
        self.missed_letters = set()
        self.set_charframe()

    def set_charframe(self):
        for index, char in enumerate(self.sparse_word):
            if char != ' ':
                self.char_frame.setdefault(char, list()).append(index)

    def play(self):
        chance = 1
        while chance < len(self.hangmans)+1:
            self.display_hangman(self.hangmans[chance])
            guess = input('Guess the letter or the entire word:')
            if guess == self.word:  # if user gussed the complete word
                return True
            if len(guess) == 1:
                chance = chance if self.update_blanks(guess) else chance + 1  # match the single char
            if all(char1 == char2 for char1, char2 in zip(self.sparse_word, self.blanks)):
                return True
        return False

    def update_blanks(self, guess: str) -> bool:
        char_indices = self.char_frame.get(guess, list())
        if not char_indices:
            self.missed_letters.add(guess)
            return False
        for index in char_indices:
            self.blanks[index] = guess
        return True

    def final_match(self, guess) -> bool:
        if all(char1 == char2 for char1, char2 in zip(self.sparse_word, self.blanks)):
            return True
        return False

    def display_hangman(self, hangman):
        lines = hangman.split('\n')
        lines[2] = lines[2] + '\t\t\t\t\t(' + self.theme + ')'
        lines[3] = lines[3] + '\t\t\tMissed Letters: ' + ','.join(self.missed_letters)
        lines[4] = lines[4] + '\t\t\tWord: ' + ''.join(self.blanks)
        print('\n'.join(lines))

    # based on the probability of winning/losing, provide the hint for the word
    def winning_probability(self) -> int:
        pass
