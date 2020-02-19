'''
zoltar5.py

Contains the class for zoltar

author: Yemi Shin and Georgia Wilson
CS 111, Fall 2018
date: 19 Nov 2018
'''
from fileProcessing import *
from random import *
from tarotcard3 import *
from graphics import *

class Zoltar:
    def __init__(self):
        '''
        Creates Zoltar instance

        PARAMETER:
            self

        INSTANCE VARIABLES:
            self.speech, string literal of zoltar's speech
            self.speech2, second string literal of zoltar's speech
            self.pool, the list of cards corresponding to the problem category the user selects
            self.win, graphics window on which zoltar is drawn
            self.prompt, the prompt that zoltar asks the user
            self.img, the image of zoltar
        '''
        self.speech = "ZOLTAR SPEAKS."
        self.speech2 = "Is there anything you would like to know... about your future? I can give you the answers... for a price."
        self.pool = []
        self.win = GraphWin("ZOLTAR",700,550)
        self.win.setCoords(0,0,7,5.5)
        self.prompt = ""
        self.img = Image(Point(3.5,3.5),"zoltar3.gif")
        self.img.draw(self.win)

    def intro(self):
        '''
        Creates and prints zoltar's introduction on graphics window

        PARAMETER:
            self

        RETURN VALUE:
            prints self.text and self.text2 on graphics window
        '''

        self.text = Text(Point(3.5,1.5),self.speech)
        self.text.setSize(18)
        self.text2 = Text(Point(3.5,1.3),self.speech2)
        self.text.draw(self.win)
        self.text2.draw(self.win)

    def ending(self):
        '''
        Creates and prints zoltar's end speech on graphics window

        PARAMETER:
            self

        RETURN VALUE:
            modifies and prints self.text2 and endtext
        '''
        #Erase previous texts on the screen.
        self.optiontext.undraw()
        self.options.undraw()
        self.category.undraw()
        self.prompt.undraw()
        self.entry.undraw()
        #Draw the new text objects.
        self.text2.draw(self.win)
        self.text2.setTextColor("#9e1717")
        self.text2.setSize(20)
        self.text2.setFace("times roman")
        self.text2.setText("Don't forget...I will be coming for your firstborn child.")
        endtext = Text(Point(3.5,1.1),"I told you there will be a price...")
        endtext.setFace("times roman")
        endtext.setTextColor("#9e1717")
        endtext.setSize(20)
        endtext.draw(self.win)

    def promptUser(self,situation):
        '''
        Prompts user for input

        PARAMETER:
            situation, situation for which zoltar prompts the user
                - situation == "problem": prompting user for problem category
                - situation == "choosenumbers": prompting user for number inputs

        RETURN VALUE:
            categorystr, problem category the user inputs
            index1, user's age
            index2, user's birth month
            index3, user's favorite number from 1 to 10
        '''
        if situation == "problem":
            self.prompt = Text(Point(3.5,1),"What kind of problem are you having?")
            self.prompt.draw(self.win)
            self.optiontext = Text(Point(3.5, 0.8), "<<Options>>")
            self.optiontext.draw(self.win)
            self.options = Text(Point(3.5, 0.6),"romance     finance     family     academic     friend")
            self.options.draw(self.win)
            self.category = Entry(Point(3.5, 0.4), 15)
            self.category.draw(self.win)
            #Keep retrieving text from entry object until user presses <Enter>
            key = self.win.getKey()
            while key != "Return":
                self.category.getText()
                key = self.win.getKey()
            categorystr = self.category.getText()
            return categorystr

        if situation == "choosenumbers":
            #Clear previous prompts
            self.text2.undraw()
            self.optiontext.undraw()
            self.options.undraw()
            self.category.undraw()
            #Draw new prompts
            #Index 1: user's age
            self.prompt.setText("How old are you?")
            self.entry = Entry(Point(3.5,0.8),10)
            self.entry.draw(self.win)
            #Keep retrieving text from entry object until user presses <Enter>
            key = self.win.getKey()
            while key != "Return":
                self.entry.getText()
                key = self.win.getKey()
            #Make sure the numbers are feasible
            index1_1 = int(self.entry.getText())
            if index1_1 <= 12: #when the age is too young that it might conflict with the birth month
                index1 = randrange(12,22)
            elif index1_1 > 22: #when the age is too old that it might conflict with the limited number of cards
                index1 = index1_1 //5
            else:
                index1 = index1_1
            #Index 2: user's birth month
            self.prompt.setText("What month were you born?(number): ")
            self.entry.setText("")
            #Keep retrieving text from entry object until user presses <Enter>
            key = self.win.getKey()
            while key != "Return":
                self.entry.getText()
                key = self.win.getKey()
            index2 = int(self.entry.getText())
            #Index 3: user's favorite number from 1 to 10
            self.prompt.setText("Enter your favorite number from 1 to 10.")
            self.entry.setText("")
            #Keep retrieving text from entry object until user presses <Enter>
            key = self.win.getKey()
            while key != "Return":
                self.entry.getText()
                key = self.win.getKey()
            index3_1 = int(self.entry.getText())
            #Make sure the numbers are not overlapping
            if index3_1 == index2:
                index3 = index3_1 + 1
            else:
                index3 = index3_1
            return index1,index2,index3

    def shuffle(self):
        '''
        Shuffles the 22 tarot cards each time the program runs

        PARAMETER:
            self

        RETURN VALUE:
            self.pool, list of cards within the problem category selected by user
        '''
        shuffle(self.pool)
        return self.pool

    def selectProblemList(self,category):
        '''
        Finds the file corresponding to the problem category selected by user and processes it into a list

        PARAMETER:
            self
            category, the problem category selected by user

        RETURN VALUE:
            self.pool, the list containing the cards
        '''
        if category == "romance":
            self.pool = processFile("romance.txt")
        elif category == "finance":
            self.pool = processFile("finance.txt")
        elif category == "family":
            self.pool = processFile("family.txt")
        elif category == "academic":
            self.pool = processFile("academic.txt")
        elif category == "friend":
            self.pool = processFile("friend.txt")
        else:
            print("You did not enter a valid category. Please try again.")
            return "badinput"
        return self.pool

    def createTarotCard(self, index):
        '''
        Creates tarot card instance

        PARAMETER:
            self
            index, the index of the card within the list self.pool

        RETURN VALUE:
            self.card, a tarot card instance
        '''
        self.card = TarotCard(index)
        return self.card

    def readFuture(self,card):
        '''
        Returns the meaning of the tarot card

        PARAMETER:
            self
            card, the tarot card instance 

        RETURN VALUE:
            meaning, the meaning of the tarot card
        '''
        meaning = card.read(self.pool)
        return meaning
