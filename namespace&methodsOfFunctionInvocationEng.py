# os - library for working with the console

import os

# Setting the font color of the console
os.system('COLOR B')


# single_root_words - function for creating a list
#                     with the same root words
def single_root_words(root_word, *other_words):
    same_words = []

    # Search for single-root words
    for word in other_words:
        if (root_word.lower() in word.lower()
                or word.lower() in root_word.lower()):
            same_words.append(word)

    return same_words


# print_root_words - function for the output of single-root words
def print_root_words(result):
    print('Single-root words: ', result, end='.\n')


# Let's find the same root words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Let's output the same-root words
print('\nDATA OUTPUT\n')
print_root_words(result1)
print_root_words(result2)
print()

try:
    os.system('PAUSE')  # Stopping the program
    os.system('CLS')  # Clearing the console screen
except:
    os.system('CLS')  # Clearing the console screen
