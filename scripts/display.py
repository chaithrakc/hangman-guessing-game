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
default_width = 50
divider = ''.ljust(default_width, '-')
theme = ''
hint = ''


def display_results(results, secret_word):
    print(divider)
    won = TerminalColors.FAIL + 'YOU WON! 😊' + TerminalColors.ENDC
    lost = f'{TerminalColors.FAIL}YOU LOST ☹️{TerminalColors.ENDC}'
    print(won.center(default_width) if results else lost.center(default_width))
    print(f'Secret Word is {TerminalColors.FAIL}{secret_word}!{TerminalColors.ENDC}'.center(default_width))
    print(divider)


def display_hangman(probability, hangmans, missed_letters, blanks):
    str_theme = '(' + theme + ')'
    str_missed_letters = 'Missed Letters: ' + ','.join(missed_letters)
    str_word = 'Word: ' + ''.join(blanks)
    lines = hangmans[len(missed_letters)].split('\n')
    lines[1] = lines[1] + str_theme.center(default_width)
    lines[2] = lines[2] + str_missed_letters.center(default_width)
    lines[3] = lines[3] + str_word.center(default_width)
    if probability < 1:
        lines[5] = lines[5] + f'{TerminalColors.OKBLUE} {hint.center(default_width)}{TerminalColors.ENDC}'
    print('\n'.join(lines))
