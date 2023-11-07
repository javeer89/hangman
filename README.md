# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 


>>> milestone_2
        random {word_generator()} that pulls a {word} from {word_list} .

>>> milestone_3
        requests for a user input {make_guess}
        it plays back 2 functions that 
            (i)     validates if it is a single letter and alphabetical chararacter
            (ii)    checks if letter exists inside of the random {word}
            (iii)   prints instructions for correction or confirms letter's existence

update!
milestone_3 is basically redundant and should be removed. lol

>>> milestone_4
        main game build. does bare stuff.
        basically,
                - we call the game.
                - then it triggers a user input for a letter
                - then that letter gets checked for validation
                - then checked against existence in game word
                - then will update the game state
                - inform player if they have been gotten the letter correct or wrong
                - if right it should return game state of word to be guessed and allow another guess
                - if wrong then it should reduce life count by 1 and allow another user input