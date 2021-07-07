class TerminalColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


already_exists = f'{TerminalColors.OKGREEN}{TerminalColors.BOLD}Already guessed that letter. Choose again.{TerminalColors.ENDC}'
theme = ''
blanks = list()
missed_letters = set()


def display_results(results, secret_word):
    print('-' * 50)
    won = f'\t\t\t{TerminalColors.FAIL}YOU WON!{TerminalColors.ENDC}'
    lost = f'\t\t\t{TerminalColors.FAIL}YOU LOST{TerminalColors.ENDC}'
    print(won if results else lost)
    print(f'\tSecret Word is {TerminalColors.FAIL}{secret_word}!{TerminalColors.ENDC}')
    print('-' * 50)


def display_hangman(hangman):
    lines = hangman.split('\n')
    lines[1] = lines[1] + '\t\t\t\t (' + theme + ')'
    lines[2] = lines[2] + '\t\t\tMissed Letters: ' + ','.join(missed_letters)
    lines[3] = lines[3] + '\t\t\tWord: ' + ''.join(blanks)
    print('\n'.join(lines))


def display_finalstate():
    lines = list()
    lines.append('-' * 50)
    lines.append('\t\t\t(' + theme + ')')
    lines.append('\t\tMissed Letters: ' + ','.join(missed_letters))
    lines.append('\t\tWord: ' + ''.join(blanks))
    print('\n'.join(lines))
