'''
Connor Brabant, Anthony DiMarco
cbraban1@binghamton.edu, adimarc1@binghamton.edu
Final Project - GUI
'''
'''
This GUI is used interactively with the imported program to create a display
that shows the user entered guesses, correct responses, and a button that
starts the game.

Output to Window:
    self.__label- title, says Play a game of Hangman
    self.__labelEnter - displays label for entrybox
    self.__labelGuesses- displays label for guesses
    self.__GuessVariableLabel = displays letter guessed
    self.__variableSorted = displays variable sorted

Input From User:
    self.__buttonStart - starts the game
    self.__EntryLabel - allows user to enter numbers


Tasks Allocated for

'''


from tkinter import *
from tkinter import messagebox
from Code import *

TURNS = 0

class GUI():

    def __init__(self):
        self.__win = Tk()
        self.__win.title('Guess the Word')
        self.__Hangman = Hangman()
        self.__label = Label(self.__win,
                             text="Let's Play Guess the Word!")
        self.__label.grid(row=0,column=0)
        self.__labelEnter = Label(self.__win,
                                text="Please enter a letter: ")
        self.__labelEnter.grid(row=2,column=0)
        self.__labelIncorrectGuesses = Label(self.__win,
                            text ="Incorrect Letters Entered: ")
        self.__labelIncorrectGuesses.grid(row=3, column=0)
        self.__labelGuessRemaining = Label(self.__win,
                            text = 'Guesses Remaining: ')
        self.__labelGuessRemaining.grid(row=4,column=0)
        self.__LabelGuesses = Label(self.__win, text='Letters in Puzzle: ')
        self.__LabelGuesses.grid(row=5,column=0)

        self.__buttonStart = Button(self.__win,
                text="Press to Start", command=self.gameButton)
        self.__buttonStart.grid(row=1,column=0)

        self.__EntryLabel = Entry(self.__win, width=2)
        self.__EntryLabel.bind('<Return>', self.entryBox)
        self.__EntryLabel.grid(row=2,column=1)

        self.__GuessVariable = StringVar()
        self.__GuessVariableLabel = Label(self.__win,
                    textvariable = self.__GuessVariable)
        self.__GuessVariableLabel.grid(row=3, column=1)

        self.__GuessRemaining = StringVar()
        self.__GuessRemainingLabel = Label(self.__win,
                    textvariable = self.__GuessRemaining)
        self.__GuessRemainingLabel.grid(row=4,column=1)

        self.__variable = StringVar()
        self.__variable.set('')
        self.__variableSorted = Label(self.__win,
                                      textvariable = self.__variable)
        self.__variableSorted.grid(row=5, column=1)

        self.__win.mainloop()

    def gameButton(self): #generates a random word from the imported list
        self.__Hangman.wordToSolve()
        if self.__Hangman.wordToSolve():
            GUI.clearAllWidgets(self)
        self.__Hangman.clearIncorrectGuessList()
        self.__Hangman.clearCorrectGuessList()
        self.__variable.set(self.__Hangman.retrieveAnswer())
        self.__GuessRemaining.set(self.__Hangman.guessesRemaining())

        #print(self.__Hangman.wordToSolve()) debug

    def clearAllWidgets(self):
        self.__Hangman.clearIncorrectGuessList()
        self.__Hangman.clearCorrectGuessList()
        self.__EntryLabel.delete(0, END)
        self.__GuessVariable.set("")
        self.__variable.set("")
        self.__GuessRemaining.set("")
    #disgards all widgets

    def entryIsLetter(self):
        lowerCaseAlphabet = ['a','b','c','d','e','f','g','h','i','j','k','l',
                           'm','n','o','p','q','r','s','t','u','v','w','x',
                           'y','z']

        EntryLabel = self.__EntryLabel.get()
        if EntryLabel in lowerCaseAlphabet:
            return True
        else:
            messagebox.showinfo('Error', '''Sorry you have entered an incorrect character!
Please try again!''')
            self.__EntryLabel.delete(0, END)

    def notDuplicate(self):
        letter = self.__EntryLabel.get()
        if letter in self.__Hangman.retrieveIncorrectList() or letter in self.__Hangman.retrieveAnswer():
            messagebox.showinfo('Error', '''Sorry you have entered a duplicate character!
            Please try again!''')
            self.__EntryLabel.delete(0, END)
        else:
            return True


    def entryBox(self, event): #utilizes entrybox to solve puzzle
        yourWord = self.__Hangman.retrieveWord()
        #print(yourWord) #debug prints randomword that was generated
        #print(len(yourWord))
        #print(self.__Hangman.retrieveAnswer())
        yourLetter = self.__EntryLabel.get()
        if GUI.entryIsLetter(self) == True and GUI.notDuplicate(self) == True:
            #print(yourLetter) #debug prints letter that was entered
            if self.__Hangman.guess(yourWord, yourLetter) == True:
                #print(self.__Hangman.find(theWord, theLetter))
                #self.__Hangman.find(yourWord, yourLetter)
                self.__Hangman.solveTheHangman(yourLetter)
                    #print(self.__Hangman.solveTheHangman(theLetter))
                self.__variable.set(self.__Hangman.retrieveAnswer())
                self.__EntryLabel.delete(0, END)
                    #print(self.__variable.set(self.__Hangman.retrieveAnswer()))
            else:
                self.__Hangman.incorrectListToAnswer()
                #print(self.__Hangman.incorrectListToAnswer())
                self.__GuessVariable.set(self.__Hangman.retrieveIncorrectResult())
                self.__EntryLabel.delete(0, END)
                self.__GuessRemaining.set(self.__Hangman.guessesRemaining())
            #print(len(self.__Hangman.retrieveIncorrectList())) debug for incorrect list
            #print(len(self.__Hangman.retrieveAnswer()))
            #if len(self.__Hangman.retrieveIncorrectList()) == 5:
            if self.__Hangman.guessesRemaining() == 0:
                messageText ='Sorry! You have ran out of turns. \nThe correct word was: {yourWord} \nWould you like to play again?'.format(yourWord = yourWord)
                response = messagebox.askyesno('You lost!', messageText)
                self.__Hangman.clearIncorrectGuessList()
                if response == False:
                    self.__win.destroy()

                else:
                    self.__Hangman.wordToSolve()
                    GUI.clearAllWidgets(self)

            elif self.__Hangman.wordGuessed() == True:
                messageText = 'You have won the game!!\nThe word you guessed was : {yourWord} \nWould you like to play again?'.format(yourWord=yourWord)
                response = messagebox.askyesno('Congrats', messageText)
                if response == False:
                    self.__win.destroy()
                else:
                    self.__Hangman.wordToSolve()
                    GUI.clearAllWidgets(self)
                #determines end of game based on length of lists
                #prompts user to play again or quit



def main():
    GUI()

main()
