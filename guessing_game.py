# Author: <Ty Wenrick>
# Assignment #4 - Guessing Game
# Date due: 2021-04-08
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

####### DO NOT EDIT CODE BELOW (changing MAX_MISSES is ok) ########
import random
import sys
import random

MAX_MISSES = 5
BORDER_LENGTH = 30
SINGLE_CHAR_LENGTH = 1


def display_game_state(chars, misses):
    """
    Displays the current state of the game: the list of characters to display
    and the list of misses.
    """

    print()
    print('=' * BORDER_LENGTH)
    print()

    print("Word:\t{}\n".format(space_chars(chars)))
    print("Misses:\t{}\n".format("".join(misses)))


####### DO NOT EDIT CODE ABOVE (changing MAX_MISSES is ok) ########


def blank_chars(word):
    """Returns a list of underscore characters with the same length as word.

    :param word: target word as a string
    :return: a list of underscore characters ('_')

    >>> blank_chars("happiness")
    ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    """
    underscore_list = []
    for i in word:
        underscore_list.append("_")

    return underscore_list


def space_chars(chars):
    """Returns a string with the characters in chars list separated by spaces.

    :param chars: a list of characters
    :return: a string containing characters in chars with intervening spaces

    >>> space_chars(['h', '_', 'p', 'p', '_', 'n', '_', '_', '_'])
    'h _ p p _ n _ _ _'
    """
    joined = " ".join(chars)
    if not chars:
        return ""
    elif len(chars) == 1:
        return ''.join(chars)
    else:
        return joined


def get_guess():
    """Prompts the user for a guess to check for the game's current word. When the user
    enters input other than a single character, the function prompts the user again
    for a guess. Only when the user enters a single character will the prompt for
    a guess stop being displayed. The function returns the single-character guess
    entered by the user.

    :return guess: a single character guessed by user
    """

    guess = input("Guess:\t")

    while True:
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            guess = input("Guess:\t")

    return guess.lower()


def check_guess(word, guess):
    """Returns a list of positions where guess is present in word.
    An empty list should be returned when guess is not a single
    character or when guess is not present in word.


    :param word: target word as a string
    :param guess: a single character guessed by user
    :return positions: list of integer positions

    >>> target_word = "happiness"
    >>> guess = 'p'
    >>> check_guess(target_word, guess)
    """
    positions = []

    if len(guess) > 1:
        return positions

    for i in range(len(word)):
        if guess == word[i]:
            positions.append(i)

    return positions


def update_chars(chars, guess, positions):
    """Updates the list of characters, chars, so that the characters
    at the index values in the positions list are updated to the
    character guess.


    :param chars: a list of characters
    :param guess: a single character guessed by user
    :param positions: list of integer positions
    :return: None
    """
    for i in range(len(positions)):
        chars[positions[i]] = guess


def add_to_misses(misses, guess):
    """Adds the character guess to the misses list.

    :param misses: list of guesses not present in target word
    :param guess: a single character guessed by user
    :return: None
    """
    misses.append(guess)


def update_state(chars, misses, guess, positions):
    """Updates the state of the game based on user's guess. Calls the function update_chars() when
    the positions list is not empty to reveal the indices where the character guess is present. Calls the
    function add_to_misses() when the positions list is empty to add guess to the misses list.

    :param chars: a list of characters
    :param misses: list of guesses not present in target word
    :param guess: a single character guessed by user
    :param positions: list of integer positions
    :return: None
    """
    if not positions:
        add_to_misses(misses, guess)
    else:
        update_chars(chars, guess, positions)


def is_round_complete(chars, misses):
    """Indicates whether or not a round has ended. This function returns True
    when the user has successfully guessed the target word or exceeds the
    number of allowed misses. Otherwise, the function returns False,
    indicating that the round is not complete. A message revealing the
    user's success or failure guessing the target word is output by this
    function when the round is complete.


    :param chars: a list of characters
    :param misses: list of guesses not present in target word
    :return status: True when round is finished, False otherwise
    """
    if len(misses) > MAX_MISSES:
        print()
        print('SORRY! NO GUESSES LEFT.')
        return True

    if chars.count('_') < 1:
        print()
        print('YOU GOT IT!')
        return True
    else:
        return False


def read_words(filepath):
    """Opens a file of word located at filepath, reads the file of words line by line,
    and adds each word from the file to a list. The list is returned by the
    function

    :param filepath: path to input file of words (one per line)
    :return word_list: list of strings contained in input file
    """
    list_of_words = []
    try:
        with open(filepath, 'r') as file:
            for line in file:
                list_of_words.append(line.strip())

        return list_of_words

    except OSError as e:
        print(e)
        return list_of_words


def get_word(words):
    """Selects a single word randomly from words list and returns it.

    :param words: list of strings
    :return word: string from words list
    """

    return words[random.randrange(0, len(words) - 1)]


def is_game_complete():
    """Prompts the user with "Play again (Y/N)?". The question is repeated
    until the user enters a valid response (one of Y/y/N/n). The function
    returns False if the user enters 'Y' or 'y' and returns True if the user
    enters 'N' or 'n'.

    :return response: boolean representing game completion status
    """
    test = True
    while test:
        play_again = input('Play again (Y/N)? ')
        print()
        if play_again == 'Y' or play_again == 'y':
            test = False
            return False
        elif play_again == 'N' or play_again == 'n':
            test = False
            return True


def run_guessing_game(words_filepath):
    """Controls running The Guessing Game. This includes parsing
    the words file and executing multiple rounds of the game.

    :param words_filepath: the location of the file of words for the game
    :return: None
    """

    try:
        with open(words_filepath) as file:
            pass

    except FileNotFoundError as f:
        print('The provided file location is not valid. Please enter a valid path to a file.')
        return None

    num_rounds = 1
    if num_rounds == 1:
        print('Welcome to The Guessing Game!')

    list_of_words = read_words(words_filepath)
    word = get_word(list_of_words)
    chars = blank_chars(word)
    misses = []
    display_game_state(chars, misses)

    while not is_round_complete(chars, misses):
        guess = get_guess()
        positions = check_guess(word, guess)
        update_state(chars, misses, guess, positions)
        display_game_state(chars, misses)

    display_game_state(word, misses)

    if not is_game_complete():
        num_rounds += 1
        run_guessing_game(words_filepath)
    else:
        print('Goodbye.')
        print()


def main():
    ########## DO NOT EDIT ASSIGNMENT STATEMENT BELOW #########

    filepath = sys.argv[-1]

    ########## DO NOT EDIT ASSIGNMENT STATEMENT ABOVE #########

    # call run_guessing_game() with filepath as argument and remove pass below

    run_guessing_game('word_file.txt')


if __name__ == '__main__':
    main()
