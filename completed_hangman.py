# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    y=get_guessed_word(secret_word,letters_guessed)

    if "_" in y:
        return False
    else:
        return True

def split(word):
    return [char for char in word]

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    y=split(secret_word)
    for char in range(len(y)):
        y[char]="_"
    if letters_guessed is None:
        return y
    else:
        for letter in range(len(letters_guessed)):
            for second in range(len(secret_word)):
                if letters_guessed[letter]== secret_word[second]:
                    y[second]=secret_word[second]
    return y


def get_available_letters(letters_guessed,not_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if letters_guessed is None:
        letters_guessed=[]

    for check in range(len(letters_guessed)):
         for letter in range(len(not_guessed)):
            if not_guessed[letter]==letters_guessed[check]:
                not_guessed.remove(letters_guessed[check])
                break
    return not_guessed

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    this_many_letters=len(secret_word)
    remaining_guesses=6
    letters_guessed = []
    letters_not_guessed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
    print("The word you need to guess has", this_many_letters, "letters")
    while remaining_guesses>0:
        print("--------------------------------------------------------------------------")
        if letters_guessed is None:
            letters_guessed=[]
        if remaining_guesses == 6:
            print("You have 6 chances to guess wrong letters")
        guess = input("what single letter do you guess? ")
        if type(guess)== str:
            if secret_word.find(guess)==-1:
                remaining_guesses+= -1
            letters_guessed.append(guess)
        else:
            print("You need to input an actual letter")
        print("You have", remaining_guesses, "guesses remaining")
        letters_not_guessed = get_available_letters(letters_guessed, letters_not_guessed)
        print("The letters you have not guessed yet are:", letters_not_guessed)
        print("Correct letters so far are ", get_guessed_word(secret_word, letters_guessed))

        if is_word_guessed(secret_word,letters_guessed):
            remaining_guesses=0
    if is_word_guessed(secret_word,letters_guessed):
        print("You win!")
    else:
        print("You get nothing. You lose. Good day Sir! ")
        print("The word was actually: ", secret_word)



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    yay=0
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if len(my_word) == len(other_word):
        for letter in range(len(my_word)):
            if my_word[letter] == "_" or my_word[letter]== other_word[letter]:
                    yay += 1
        if yay==len(my_word):
            return True
        else:
            return False
    else:
        return False




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Possible answers are:")
    for word in range(len(wordlist)):
        if match_with_gaps(my_word, wordlist[word]) == True:
            print(wordlist[word], end=' ')
    print("")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    this_many_letters = len(secret_word)
    remaining_guesses = 6
    letters_guessed = []
    letters_not_guessed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v',
                           'w', 'x', 'y', 'z']
    print("The word you need to guess has ", this_many_letters, " letters")
    while remaining_guesses > 0:
        print("--------------------------------------------------------------------------")
        if letters_guessed is None:
            letters_guessed = []
        if remaining_guesses == 6:
            print("You have 6 chances to guess wrong letters")
        guess = input("what single letter do you guess? ")
        if type(guess) == str and guess!="*":
            if secret_word.find(guess) == -1:
                remaining_guesses += -1
            letters_guessed.append(guess)
        elif guess!="*":
            print("You need to input an actual letter")
        print("You have", remaining_guesses, " guesses remaining")
        letters_not_guessed = get_available_letters(letters_guessed, letters_not_guessed)
        print("The letters you have not guessed yet are: ", letters_not_guessed)
        print("Correct letters so far are ", get_guessed_word(secret_word, letters_guessed))
        if guess== "*":
            show_possible_matches(get_guessed_word(secret_word,letters_guessed))
        if is_word_guessed(secret_word, letters_guessed):
            remaining_guesses = 0
    if is_word_guessed(secret_word, letters_guessed):
        print("You win!")
    else:
        print("You get nothing. You lose. Good day Sir! ")
        print("The answer was ", secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
     pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#secret_word = choose_word(wordlist)
#hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
