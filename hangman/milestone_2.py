'''This Document will contain a series of words
that are to be used for the aiCore Hangman Project'''
#%%
import random

word_list = ["Banana", "Apple", "Orange", "Pear", "Kiwi"]
#print(word_list)

word = random.choice(word_list)
#print(word)

inputGuess = False
while inputGuess == False:
    guess = input("Guess a letter")
    if len(guess) == 1 and guess.isalpha() == True:
        inputGuess = True
        print("Good guess!")
        print("Your letter is "+ guess)
    else: 
        print("Oops! That is not a valid input")
        

