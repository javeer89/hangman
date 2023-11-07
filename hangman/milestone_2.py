'''This Document will contain a series of words
that are to be used for the aiCore Hangman Project'''
#%%
list_of_words = ["banana", "apple", "orange", "pear", "kiwi"]

def word_generator():
    import random
    word_gen = random.choice(list_of_words)
    return word_gen
