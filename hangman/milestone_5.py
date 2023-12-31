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

#Check guessed letter
    def check_guess(self, guess):
        print("Your guess is "+ guess)
        inputGuess = False        
        while inputGuess == False:
            if len(guess) == 1 and guess.isalpha() == True:
                inputGuess = True
                self.guesses_update(guess)
                if guess in self.word_list:
                    print(f"Good guess! {guess} is in the word.")
                    self.guess_correct(guess)
                else:
                    print(f"Sorry, {guess} is not in the word. Try again.")
                    self.guess_wrong(guess)
                    #self.game_state_lose(guess)
            else:
                print("Oops! That is not a valid input. PLEASE INPUT A CORRECT LETTER!")
                break

    def guesses_update(self, guess):
        self.guesses.append(guess)

    def guess_correct(self, guess):
        for i in range(self.word_len):   
            if(self.word_list[i] == guess):
                self.word_to_be_guessed[i] = guess
        print(f"Guessing Progress: {self.word_to_be_guessed}")
        print(f"Your Guesses so far: {self.guesses}")
    
    def guess_wrong(self, guess):
        self.num_lives = self.num_lives - 1
        print(f"You have {self.num_lives} lives remaining.")
        print(f"Guessing Progress: {self.word_to_be_guessed}")
        print(f"Your Guesses so far: {self.guesses}")
        print("TRY AGAIN--------------------- ")

#Request a letter to be guessed
    def ask_letter(self):
        guess = input("Guess a letter").lower()
        if guess in self.guesses:
            print ("You have used that letter. Please try again")
        else:    
            self.check_guess(guess)

        
#PLAY GAME
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while game.num_lives > 0 and game.word_to_be_guessed.count("_") > 0:
        game.ask_letter()

        if game.num_lives == 0:
            print(f"You lost! Muhuhahahaha")

        if game.word_to_be_guessed.count("_") == 0:
            print("Congratulations, you won!")

play_game(word_list)


