#%%

import random
from milestone_2 import list_of_words

word_list = list_of_words

class Hangman():
#Parameters
    def __init__(self, word_list, num_lives=5):
#Attributes
        
        self.word_sourced = (random.choice(list_of_words)).lower()
        self.word = self.word_sourced
        self.word_list = list(self.word)
        self.word_len = len(self.word)
        self.word_index = list(range(len(self.word)))
        self.num_lives = num_lives
        self.num_letters = len(self.word)
        self.word_to_be_guessed = ['_'] * len(self.word)
        self.guesses = []


#Prints to be deleteed.
        print(f"Sourced word: {self.word_sourced}.")
        print(f"Your word: {self.word}.")
        print(f"List form: {self.word_list}.")
        print(f"Word Length: {self.word_len}.")
        print(f"Index form: {self.word_index}.")
        print(f"You have {self.num_lives} lives.")
        print(f"There are {self.num_letters} letters to find.")
        print(f"Letters of the word guessed, so far: {self.word_to_be_guessed}.")
        print(f"Your guesses have been: {self.guesses}.")
#Prints to be deleteed.

#Check guessed letter
    def check_guess(self, guess):
        #guess = input("Guess a letter")
        guess = str.lower(guess)
        print("Your guess is "+ guess)
        inputGuess = False
        
        while inputGuess == False:
            if len(guess) == 1 and guess.isalpha() == True:
                inputGuess = True
                wordCheck = False
                self.guesses_update(guess)
                if wordCheck == False:
                    if guess in word_list:
                        print(f"Good guess! {guess} is in the word.")
                        wordCheck = True
                        #self.guess_correct(guess)
                        #print(f"Your Guesses so far: {guess}")
                    else:
                        print(f"Sorry, {guess} is not in the word. Try again.")
                        #self.guess_wrong(guess)
                        #print(f"we've entered the wrong timeline")
                        #print(f"Your Guesses so far: {guess}")
                        #print(f"Guessing Progress: {self.word_to_be_guessed}")
                        #self.game_state_lose(guess)
            else:
                print("Oops! That is not a valid input")
                break

    def guesses_update(self, guess):
        self.guesses.append(guess)
        print(f"Your guesses so far: {self.guesses}")

    def guess_correct(self, guess):
        for i in range(self.word_len):   
            # check the condition
            if(self.word_list[i] == guess):
                print(i)
                self.word_to_be_guessed[i] = guess
        print(f"Guessing Progress: {self.word_to_be_guessed}")
    
    def guess_wrong(self, guess):
        self.num_lives = self.num_lives - 1
        print(f"You have {self.num_lives} lives remaining.")
        return

    #def game_state()

    #Request a letter to be guessed
    def ask_letter(self):
        guess = input("Guess a letter")
        #self.guesses.append(str.lower(guess))
        self.check_guess(guess)
        

Hangman(word_list,5)