'''This document checks an input for being a single letter and a alphabetical.'''
#%%
#imported functions (word_generator) and variables (new_word & nwl (new word as a list)).
from milestone_2 import word_generator

def guess_word():
    print("Your guess is "+ guess)
    inputGuess = False
    while inputGuess == False:
        if len(guess) == 1 and guess.isalpha() == True:
            inputGuess = True
            if inputGuess == True:
                if guess in word_list:
                    print(f"Good guess! {guess} is in the word.")
                else:
                    print(f"Sorry, {guess} is not in the word. Try again.")
        else:
            print("Oops! That is not a valid input")
            break   

def check_guess():
    guess_word()
    print("word: "+ str(word))

guess = input("Guess a letter").lower()
word = word_generator()
word_list = list(word)

check_guess()