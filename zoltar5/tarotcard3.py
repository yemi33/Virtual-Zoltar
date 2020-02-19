'''
zoltar_simulation_ver3.py

Contains the class for tarot card

author: Yemi Shin and Georgia Wilson
CS 111, Fall 2018
date: 19 Nov 2018
'''
from graphics import *

class TarotCard:
    def __init__(self,indexNumber):
        '''
        Creates an instance of a Tarot Card.

        PARAMETER:
            indexNumber, the index of the card within a problem category

        INSTANCE VARIABLES:
            self.indexNumber, indexNumber
            self.name, string value of the card name
            self.meaning, string that holds the meaning of the card
            self.img, graphic image of the front side of the card
            self.bimg, graphic image of the back side of the card
            self.orientation, indicator of whether or not the card is facing up or down
        '''

        self.indexNumber = indexNumber
        self.name = "card"
        self.meaning = ""
        self.img = ""
        self.bimg = ""
        self.orientation = "back"

    def getIndex(self):
        '''
        Returns the index of the card within a problem category

        PARMETER:
            self

        RETURN VALUE:
            self.indexNumber, indexNumber
        '''
        return self.indexNumber

    def getOrientation(self):
        '''
        Returns the current orientation of the card

        PARAMETER:
            self

        RETURN VALUE:
            self.orientation, current orientation of the card
        '''
        return self.orientation

    def getName(self,list):
        '''
        Returns the name of the card

        PARAMETER:
            self
            list, list of cards corresponding to the problem category the user selects

        RETURN VALUE:
            self.name, string literal of the card name
        '''
        n = list[self.indexNumber].split(":")
        self.name = n[0]
        return self.name

    def read(self,list):
        '''
        Returns the meaning of the card

        PARAMETER:
            self
            list, the list of cards corresponding to the problem category the user selects

        RETURN VALUE:
            self.meaning, string literal of the card meaning
        '''
        m = list[self.indexNumber].split(":")
        self.meaning = m[1]
        return self.meaning

    def createCardImage(self,win,x,y,list):
        '''
        Draws the front side image of the card on graphics window

        PARAMETER:
            win, graphics window
            x, x position of the anchorpoint for image
            y, y position of the anchorpoint for image
            list, the list of cards corresponding to the problem category the user selects

        RETURN VALUE:
            draws card image on graphics window
        '''
        i = list[self.indexNumber].split(":")
        filename = i[2]
        filename = filename.strip("\n")
        img = Image(Point(x,y),filename)
        img.draw(win)

    def createBackImage(self,win,x,y):
        '''
        Draws the back side image of the card on graphics window

        PARAMETER:
            win, graphics window
            x, x position of the anchorpoint for image
            y, y position of the anchorpoint for image

        RETURN VALUE:
            draws back card imag on graphics window
        '''
        self.bimg = Image(Point(x,y), "tarotbackdesign2.gif")
        self.bimg.draw(win)

    def flipCard(self, win, thcard):
        '''
        Flips the nth card

        PARAMETER:
            win, graphics window
            thcard, the order of the card

        RETURN VALUE:
            undraws back side image of the card to reveal front side image
        '''
        click = win.getMouse()
        clickx = click.getX()
        clicky = click.getY()
        if thcard == 1:
            while self.orientation == "back":
                if clickx < 2.73 and clickx > 1.27 and clicky <= 4.7 and clicky >= 2.3:
                    self.orientation = "front"
                    self.bimg.undraw()
                else:
                    click = win.getMouse()
                    clickx = click.getX()
                    clicky = click.getY()
        elif thcard == 2:
            while self.orientation == "back":
                if clickx <= 4.73 and clickx >= 3.27 and clicky <= 4.7 and clicky >= 2.3:
                    self.orientation = "front"
                    self.bimg.undraw()
                else:
                    click = win.getMouse()
                    clickx = click.getX()
                    clicky = click.getY()
        elif thcard == 3:
            while self.orientation == "back":
                if clickx <= 6.73 and clickx >= 5.27 and clicky <= 4.7 and clicky >= 2.3:
                    self.orientation = "front"
                    self.bimg.undraw()
                else:
                    click = win.getMouse()
                    clickx = click.getX()
                    clicky = click.getY()
