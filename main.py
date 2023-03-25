# Programm: Word guessing game / hangman for programming languages
# Author: Stefan Schultz

import random

def readWordsFromTextFile(file_name):
    '''Read words from file by given file name.
    '''
    words = []
    
    # Read all words from file
    with open(file_name, 'r') as file:
        data = file.read().splitlines()
    
    # Split words and add to array
    for line in data:
        word = line.split(',')
        words.append(word[0])
    
    return words

# First read all words from the text file.
words_programming_languages = readWordsFromTextFile('words_programming_languages.txt')

# The program ask for the users name.
user_name = input("Tell me your name for the game? ")

# Simple hello output for motivation, before the starts.
print(f"\nGood luck and have fun {user_name}. :-)")

# Random function select a word for the game.
selected_word = random.choice(words_programming_languages)

guesses = ''
game_rounds = 16

print(f'\nWe are looking for a programming language. Guess all {len(selected_word)} characters.')

while game_rounds > 0:
    # Count the number of game rounds, where the user fails.
    failed_rounds = 0
    
    characters = ''
    for char in selected_word:
        if char in guesses:
            # print(char, end=' ')
            characters += (char + ' ')
        else:
            # print('_')
            characters += '_ '
            failed_rounds += 1
    
    print(characters)
    
    if failed_rounds == 0:
        print('\nVery nice, you win the game.')
        print(f'The programming language you are looking for is {selected_word}')
        break;
    
    print()
    guess = input('Guess the next character: ')
    guesses += guess
    
    if guess not in selected_word:
        game_rounds -= 1 
        print(f'That\'s is wrong. You have {game_rounds} attempts left')
        
        if game_rounds == 0:
            print(f'\nOh crap, you lost the game. The programming language was {selected_word}')
