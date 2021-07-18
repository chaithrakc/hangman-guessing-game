import os

default_width = 50
divider = ''.ljust(default_width, '-')
theme = ''
hint = ''


def display_results(results, secret_word) -> None:
    print(divider)
    won = 'Congratulations, You Won!'
    lost = 'You Lost the Game!'
    print(won.center(default_width) if results else lost.center(default_width))
    print(f'Secret Word is {secret_word}!'.center(default_width))
    print(divider)


def display_hangman(hangmans, missed_letters, blanks) -> None:
    #clear_console()
    str_theme = '(' + theme + ')'
    str_missed_letters = 'Missed Letters: ' + ','.join(missed_letters)
    str_word = 'Word: ' + ''.join(blanks)
    lines = hangmans[len(missed_letters)].split('\n')
    lines[1] = lines[1] + str_theme.center(default_width)
    lines[2] = lines[2] + str_missed_letters.center(default_width)
    lines[3] = lines[3] + str_word.center(default_width)
    lines[5] = lines[5] + hint.center(default_width)
    print('\n'.join(lines))


def clear_console() -> None:
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
