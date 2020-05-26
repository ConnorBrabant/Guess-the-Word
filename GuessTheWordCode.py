'''
This program simulates a game of hangman using class called Hangman,
taking in entered letters from an attached GUI and matching them with
the according word.It filters the entered letters by correctness, either
displaying them in the GUI on the lines, or adding them to the list of
wrong guesses.
'''

import random
import math

class Hangman:
    '''constructor'''
    def __init__(self):
        self.__word = ''
        self.__list = []
        self.__incorrectList = []
        self.__incorrectResult = ''
        self.__wordResult = '_ ' * (len(self.__word) - 1)

    '''accessors'''
    def retrieveWord(self):
        return self.__word

    def retrieveList(self):
        return self.__list
    def useless(self):
        return 'f'
    def retrieveAnswer(self):
        return self.__wordResult

    def retrieveIncorrectList(self):
        return self.__incorrectList

    def retrieveIncorrectResult(self):
        return self.__incorrectResult
    '''mutators'''

    def wordGuessed(self):
        if self.__wordResult.count('_') == 0:
            return True

    def clearIncorrectGuessList(self):
        self.__incorrectList = []
        return self.__incorrectList

    #clears the list of incorrect guesses from previous game

    def clearCorrectGuessList(self):
        self.__wordResult = '_ ' * (len(self.__word)-1)
        return self.__wordResult

    def guessesRemaining(self):

        if len(self.__word) >= 10:
            guessesRemaining = math.ceil((len(self.__word)/2) - len(self.__incorrectList))
        else:
            guessesRemaining = 5 - len(self.__incorrectList)
        return guessesRemaining

    #clears correct guesses from last game

    def wordToSolve(self):
        wordList = open('wordslist.txt', 'r').readlines()
        self.__word = random.choice(wordList)
        return self.__word

#opens a precreated file contain words that can be used as the hangman

    def guess(self, word, inputLetter):
        self.__list = []

        if inputLetter in word:
          self.__list = [index for index, letter in enumerate(word)
                         if letter == inputLetter]
          self.incorrectList = [0]
          return True
        else:
          self.__list = [0]
          self.__incorrectList.append(inputLetter)
          return False
    '''compares the letter entered by the user and random word
    generated from the function above to determine where in the
    word the letter is and then adjusts the list or adds an incorrect
    guess to the incorrect list'''

    def solveTheHangman(self, letterFromEntry):
        newString = ""
        textList = list(self.__wordResult)
        self.__list = self.retrieveList()

        #self.__list receives input from find function and
        #then uses these characters to solve hangman
        positionInList = self.__list
        for eachLetter in positionInList:
            textList[eachLetter * 2] = letterFromEntry
            newString = ''.join(textList)
            self.__wordResult = newString


#takes the entered letter and adds it to the result to display to the GUI
 #   the correct letters that were entered'''

    def incorrectListToAnswer(self):
       incorrectString = ""
       for each in self.__incorrectList:
           incorrectString = incorrectString + each
           self.__incorrectResult = incorrectString


    '''accumulates the wrong guesses to later show them on GUI'''
