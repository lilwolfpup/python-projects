# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
#from ps4a import get_permutations
import re


### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text=text
        self.valid_words=load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        copy=self.valid_words
        return copy
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        permutationnnnnn= list(vowels_permutation)
        a = permutationnnnnn[0]
        e = permutationnnnnn[1]
        i = permutationnnnnn[2]
        o = permutationnnnnn[3]
        u = permutationnnnnn[4]

        transpose_dict= {'a':a,'e': e,'i':i,'o':o,'u':u}
        return transpose_dict

    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        a=list(self.message_text)
        for character in range(len(a)):
            if a[character] in VOWELS_LOWER:
                boopy=transpose_dict.get(a[character])
                a[character]= boopy
        fusion=""
        return fusion.join(a)
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text= text
        self.valid_words=load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        a=[]
        this_one=""
        all_permutations= get_permutations('aeiou',a, step=0)
        best=0
        for too_much_trouble in range(len(all_permutations)):
            too_long=SubMessage.apply_transpose(self,SubMessage.build_transpose_dict(self.message_text,all_permutations[too_much_trouble]))
            too_long_copy=too_long
            regex = re.compile('[^a-zA-Z ]')
            # First parameter is the replacement, second parameter is your input string
            too_long=regex.sub('', too_long)
            # Out: 'abdE'
            too_long=too_long.lower()
            split_too_long= too_long.split()
            local_best = 0
            for shorter_list in range(len(split_too_long)):
                if split_too_long[shorter_list] in self.valid_words:
                    local_best+=1
                if local_best>best:
                    best=local_best
                    this_one=too_long_copy
        return this_one


def get_permutations(sequence, a, step=0):
    if step == len(sequence):
            # we've gotten to the end, print the permutation
        a.append(''.join(sequence[:]))
        return a
    for i in range(step, len(sequence)):
            # copy the string (store as array)
        string_copy = [c for c in sequence]
            # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
            # recurse on the portion of the string that has not been swapped yet
        get_permutations(string_copy, a, step + 1)
    return a



if __name__ == '__main__':

    # Example test case
    message = SubMessage("The fox jumped over the moon")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
