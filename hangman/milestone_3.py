'''This document checks an input for being a single letter and a alphabetical.'''
#%%
#imported functions (word_generator) and variables (new_word & nwl (new word as a list)).

def guess_word():
    inputGuess = False
    while inputGuess == False:
        guess = input("Guess a letter")
        guess = guess.lower()
        if len(guess) == 1 and guess.isalpha() == True:
            inputGuess = True
            print("Your guess is "+ guess)
            return guess
        else: 
            print("Oops! That is not a valid input")

def check_guess():
    from milestone_2 import word_generator
    word = word_generator()
    word_list = list(word)
    guess = guess_word()
    if guess in word_list:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def make_guess():
    check_guess()
    return

make_guess()




