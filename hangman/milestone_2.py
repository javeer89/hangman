'''This Document will contain a series of words
that are to be used for the aiCore Hangman Project'''
#%%
word_list = ["banana", "apple", "orange", "pear", "kiwi"]

def word_generator():
    import random
    word_gen = random.choice(word_list)
    return word_gen
