class Hangman:
    def __init__(self, word_hint: tuple, hangmans: list, theme: str):
        self.word, self.hint = word_hint
        self.encrypted_word = '_ ' * len(self.word)
        self.hangmans = hangmans
        self.theme = theme
        self.missed_letters = set()

    # based on the probability of winning/losing, provide the hint for the word
    def winning_probability(self) -> int:
        pass

    def play(self):
        for hangman in self.hangmans:
            self.display(hangman)
            guess_word = input('Guess the letter or the entire word:')

    def display(self, hangman):
        lines = hangman.split('\n')
        lines[2] = lines[2] + '\t\t\t       (' + self.theme + ')'
        lines[3] = lines[3] + '\t\t\tMissed Letters: ' + ','.join(self.missed_letters)
        lines[4] = lines[4] + '\t\t\tWord: ' + self.encrypted_word
        print('\n'.join(lines))
