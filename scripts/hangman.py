class Hangman:
    def __init__(self, input_word: dict, hangmans: list):
        self.word_hint = input_word
        self.hangmans = hangmans

    def play(self):
        for hangman in self.hangmans:
            print(hangman)
        for word, hint in self.word_hint.items():
            print(word + ' - ' + hint)
