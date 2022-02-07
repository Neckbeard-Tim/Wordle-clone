from time import time
import random, math
from venv import main

fullMatch = "✓" # Used when the letter is correct.
partialMatch = "!" # Used when the letter in that position is in the word, but not in the right position.
noMatch = "x" # Used when the letter in that position doesn't match anything in the word.

def get_Words(): # Loads every word from sgb-words.txt
    with open('sgb-words.txt','r') as f:
        words = f.read().splitlines()
    return words

def getRandomWord(wordList):
    random.seed()
    randomWord = random.choice(wordList).lower()
    return randomWord

def matchingLetters(word1,word2): # Returns the number of matching letters between two words
    matchString = ""
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            matchString += "✓"
        elif (word1[i] in word2):
            matchString += "!"
        else:
            matchString += "X"

    return matchString

def main():
    guessesLeft = 6 # controls our main loop
    hasWon = False # controls our main loop
    randomWord = getRandomWord(get_Words())
    clue = "....."
    while (guessesLeft > 0) and not hasWon:
        
        guess = input("Enter word: ").lower()
        # print("debug:", randomWord)
        if guess == randomWord:
            hasWon = True
        elif (guess in get_Words()):
            print(matchingLetters(guess, randomWord), " letters match.")
            guessesLeft -= 1
            print("Wrong answer! ", guessesLeft, " attempts remaining!")
        else:
            print("Word not recognized.")
    if hasWon:
        print("Congratulations! You won!")
        time.sleep(5)
    else:
        print("Better luck next time!")
        time.sleep(5)

main()