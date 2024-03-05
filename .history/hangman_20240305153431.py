import time
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
   
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    
    
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
    for char1 in secret_word:
        same=False
        for char2 in letters_guessed:
            if char1 == char2:
              same = True
              break
        if not same:
          return False
    return True

        
        

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    correct_letters = []
    not_guessed = []
    chances = 6
    non_repeated_guesses = list(set(letters_guessed))

    for char in non_repeated_guesses:
        if not char in secret_word:
            chances -= 1            

    for char1 in secret_word:
        for char2 in letters_guessed:
            if char1 == char2:
                correct_letters.append(char1)

    for char1 in secret_word:
        if not (char1 in correct_letters):
            not_guessed.append(char1)

    partial_word = []
    for char1 in secret_word:
        if char1 in correct_letters:
            partial_word.append(char1)
        elif char1 in not_guessed:
            partial_word.append("_")

    return (partial_word, chances)
    

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    

    letters_remained = []

    for char in abc:
        if not char in letters_guessed:
            letters_remained.append(char)

    return letters_remained



def restart_game():
  answer = input("Do you want to play again? Type 'yes'or 'no': ")
  if answer == "yes":
      welcome_to_game()
  elif answer == "no":
      print("See you next time!")
      return True
  else:
      print("I don't understand... Please type yes or no.")
      restart_game()
      
def welcome_to_game():
    letters_guessed = []
    wrong_guesses = []   
    secret_word = choose_word(wordlist)
    print("______________________WELCOME TO HANGMAN GAME______________________")
    time.sleep(1)
    user_name = input("How would you like to be called? ")
    time.sleep(1)
    print(f"Very well, dear {user_name}, shall we get started? First of all, if you want to quit the game, just type the word 'quit' and hit enter.")
    time.sleep(1)
    print("Only type one letter at a time. No numbers allowed! And if you want to know which letters you have left, type the word 'letters' and hit enter.")
    time.sleep(1)
    print("LET THE GAME BEGIN!")
    print("........*........*........*........*........*........*........*........")

    hangman(letters_guessed, wrong_guesses, secret_word)

def hangman(letters_guessed, wrong_guesses, secret_word):
    

    letter_guessed = input("Make a guess: ")
    def verify_input(input):
        if input == "letters":
            print("______________________________________________")
            print("Here is a list of letters you still haven't tried:")
            print(get_available_letters(letters_guessed))
            print("______________________________________________")
            return True
        
        if input == "quit":
            exit()
            
        if len(input) != 1 or not isinstance(input, str) or input not in abc:
            return False
        return True
        
    is_input_correct = verify_input(letter_guessed)

    while not is_input_correct:
        print("!!!!!!!....................!!!!!!!!....................!!!!!!!!")
        print("You should only write letters and one at a time.")
        letter_guessed = input("Make a guess: ")
        is_input_correct = verify_input(letter_guessed)
   
    if not letter_guessed in secret_word and not letter_guessed in wrong_guesses:
        wrong_guesses.append(letter_guessed)

    letters_guessed.append(letter_guessed)

    partial_word, chances = get_guessed_word(secret_word, letters_guessed)
    print(wrong_guesses)
    print(partial_word)
    print("The number of letters in the secret word is: ", len(secret_word))
    print(f"You have {chances} guesses remaining.")

    if chances == 0:       
        print("Oh no! You lost... Better luck next time.")
        print(f"The word we were looking for was: {secret_word.upper()}")
        restart_game()

        return True

    if chances>0:
        if not "_" in partial_word:
            print("Congratulations! You won the game!")
            restart_game()
            return True
        else:
            hangman(letters_guessed, wrong_guesses, secret_word)



if __name__ == "__main__":
    letters_guessed = []
    wrong_guesses = []   
    abc ="abcdefghijklmnopqrstuvwxyz" 
  
    
    welcome_to_game()
    
    
    
