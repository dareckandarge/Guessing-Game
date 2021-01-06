import random
import sys

MAX_MISSES = 5
BORDER_LENGTH = 30
SINGLE_CHAR_LENGTH = 1


def blank_chars(target_word):
    """
    changes the characters in a word in to a list of "_"

    param: target_word
    return: list of "_" that is length of target word
    """
    new_word = "_"
    list = []
    for letters in range(0, len(target_word)):
        # goes through word and replaces them with "_"
        new_word = new_word.replace(target_word[letters], "_")
        list.append(new_word)        # adds them to a list
        letters += 1
    return list


def space_chars(chars):
    """
    characters in a list are changed to a string separated by spaces

    param: list of characters
    return: string separated with spaces
    """
    string = " "
    new = string.join(chars)
    return new


def get_guess():
    """
    asks the user for a guess

    param: none
    return: single-character(lower case) guessed by user
    """
    guess = input("Guess:\t")
    while guess:
        if not guess.isalpha() or not len(guess) == 1:
            # check if character is not a letter and single
            return get_guess()
        else:
            return guess.lower()


def check_guess(word, guess):
    """
    returns index positions where guesses are found in target word

    param: word = target word; guess = letter guessed by user
    return: a list of index positions where guess is found
    """
    list = []
    for letter in range(len(word)):
        # iterates through word and checks if any chars match with guess
        if word[letter] == guess and len(guess) == 1:
            list.append(letter)    # adds matching characters to list
    return list


def update_chars(chars, guess, positions):
    """
    updates string so it has all the guesses at the corresponding indexes

    param: chars= list of characters; guess= list of missed guesses; positions= integer positions of correctly guessed words
    return: none
    """
    for items in positions:
        chars[items] = guess


def add_to_misses(misses, guess):
    """
    guessed missed are added to a list

    param: misses = list of missed character guesses; guess= character guessed by user
    return: none
    """
    misses.append(guess)


def update_state(chars, misses, guess, positions):
    """
    calls update_chars() and add_to_misses() functions to show the user what letters they have
    guessed right and what they have missed

    param: chars= list of characters; misses= list of letters missed; guess= character missed by user;
            position= list of integer positions of right guesses
    return: none
    """
    if positions == []:
        # if right guess positions list is empty
        add_to_misses(misses, guess)
    else:
        # if positions list has values
        update_chars(chars, guess, positions)


def is_round_complete(chars, misses):
    """
    return true when user guesses word or is out of guesses;
    otherswise returns false

    param: chars= list of characters; misses= list of missed words
    return: True or False
    """
    if len(misses) > MAX_MISSES:
        # checks if length of missed words list is longer than max_misses (5)
        print("")
        print("SORRY! NO GUESSES LEFT.")
        return True
    elif "_" not in chars:
        # checks if user has guessed all words
        print("")
        print("YOU GOT IT!")
        return True
    else:
        return False

def read_words(filepath):
    """
    opens and reads a file and adds each word to a list

    param: filepath
    return: list of words from file
    """
    file = open(filepath, "r")
    characters = []
    for line in file:
        # goes through list and adds words to list
        letter = line.strip()
        characters.append(letter)

    file.close()
    return characters


def get_word(words):
    """
    selects a random word from the list of words

    param: list of words
    return: random word
    """
    random_index = random.randrange(0, len(words)-1)
    return words[random_index]

def is_game_complete():
    """
    prompts the user to play again after each round

    param: none
    return: True or False
    """
    prompt = True
    while prompt:
        start_over = input("Play again (Y/N)? ")
        if start_over == "Y" or start_over == "y" or start_over == "N" or start_over == "n":
            # returns prompt when an invalid input in imputed
            prompt = False
            if start_over == "N" or start_over == "n":
                # stops playing if entered "N" or "n"
                return True
            elif start_over == "Y" or start_over == "y":
                # continues another round if entered "Y" or "y"
                return False


def run_guessing_game(words_filepath):
    """
    executes the guessing game by calling functions

    param: filepath address
    return: none
    """
    if True:
        # checks if text provided is a valid input; if not it prints out an error message
        try:
            read_words(words_filepath)
        except FileNotFoundError:
            print("The provided file location is not valid. Please enter a valid path to a file.")
            return False

    print("Welcome to The Guessing Game!")
    read = read_words(words_filepath)
    word = get_word(read)
    chars = blank_chars(word)
    misses = []
    display_game_state(chars, misses)


    while is_round_complete(chars, misses) == False:
        # carries out one round of the guessing game
        guess = get_guess()
        where = check_guess(word, guess)
        update_state(chars, misses, guess, where)
        is_round_complete(chars, misses)
        display_game_state(chars, misses)


    while is_game_complete() == False:
        # prompts the user to play again;
        read = read_words(words_filepath)
        word = get_word(read)
        chars = blank_chars(word)
        misses = []
        display_game_state(chars, misses)

        while is_round_complete(chars, misses) == False:
            # takes care of another round of the game
            guess = get_guess()
            where = check_guess(word, guess)
            update_state(chars, misses, guess, where)
            is_round_complete(chars, misses)
            display_game_state(chars, misses)
    # if user enters "n" or "N" game ends and prints "Goodbye!"
    print("")
    print("Goodbye.")




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


def main():

    filepath = sys.argv[-1]

    # call run_guessing_game() function to play guessing game
    run_guessing_game(filepath)


if __name__ == '__main__':
    main()
