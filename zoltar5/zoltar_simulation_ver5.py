'''
zoltar_simulation_ver5.py

Contains the simulation for the virtual Zoltar

author: Yemi Shin and Georgia Wilson
CS 111, Fall 2018
date: 19 Nov 2018
'''
from tarotcard3 import *
from zoltar_version5 import *

def simulation():
    '''
    Simulates virtual Zoltar
    '''

    #Create Zoltar
    zoltar = Zoltar()
    #Zoltar's Introduction
    zoltar.intro()

    #Ask user what category their problem falls under
    problem = zoltar.promptUser("problem")
    print("You chose: ",problem)
    ProblemList = zoltar.selectProblemList(problem)

    #Ask the user for three numbers(age,birth month,favorite number) and save them as the three indices
    i1,i2,i3 = zoltar.promptUser("choosenumbers")

    #Create the list with all Tarot card meanings depending on problem category
    print()
    print("***Gathering all the energies of the universe...***")
    print()

    #Shuffle the list
    ProblemList = zoltar.shuffle()

    #Create Tarot cards depending on given indices
    first = zoltar.createTarotCard(i1)
    second = zoltar.createTarotCard(i2)
    third = zoltar.createTarotCard(i3)

    #Find meanings for each card
    m1 = zoltar.readFuture(first)
    m2 = zoltar.readFuture(second)
    m3 = zoltar.readFuture(third)

    #Create graphics window for card display
    win2 = GraphWin("CARDS",800,500)
    win2.setCoords(0,0,8,5)
    back = Image(Point(4,2.5),"rug_background_dark.gif")
    back.draw(win2)

    #Labels for each card on graphics window
    past = Text(Point(2,1.8),"PAST")
    past.setSize(20)
    past.setFace("times roman")
    past.setTextColor("white")
    past.draw(win2)

    present = Text(Point(4,1.8),"PRESENT")
    present.setSize(20)
    present.setFace("times roman")
    present.setTextColor("white")
    present.draw(win2)

    future = Text(Point(6,1.8),"FUTURE")
    future.setSize(20)
    future.setFace("times roman")
    future.setTextColor("white")
    future.draw(win2)

    #Draw front side images of cards on graphics window
    im1 = first.createCardImage(win2,2,3.5,ProblemList)
    im2 = second.createCardImage(win2,4,3.5,ProblemList)
    im3 = third.createCardImage(win2,6,3.5,ProblemList)

    #Draw back side images of cards on graphics window to mask front side images
    bi1 = first.createBackImage(win2, 2, 3.5)
    bi2 = second.createBackImage(win2,4,3.5)
    bi3 = third.createBackImage(win2,6,3.5)

    #Prompt user to "flip" the cards in order
    prompt = Text(Point(4,1),"Flip the Past Card.") #past
    prompt.setTextColor("white")
    prompt.setSize(22)
    prompt.setFace("times roman")
    prompt.draw(win2)
    first.flipCard(win2,1)
    prompt.setText("Flip the Present Card.") #present
    second.flipCard(win2,2)
    prompt.setText("Flip the Future Card.") #future
    third.flipCard(win2,3)

    #Direct user to look at python shell for card readings
    prompt.setText("See your reading on the other screen.")

    '''Card Reading Display on Python Shell'''
    #Find the name of each card
    name1 = first.getName(ProblemList)
    name2 = second.getName(ProblemList)
    name3 = third.getName(ProblemList)

    #Print the names of the selcted cards
    print("Your cards are: ", name1,",",name2, "and", name3)
    print()

    #Print the meanings of each cards (aka user's fortune)
    print("Your past holds: ","\n",m1,"\n")
    print("Your present holds: ","\n",m2,"\n")
    print("Your future holds: ","\n",m3,"\n")

    #Direct user to look at Zoltar's final message on another graphics window
    print("------------WAIT! BEFORE YOU LEAVE...------------")
    print("    **Zoltar has one final message for you...**   ")

    #Zoltar's Conclusion
    zoltar.ending()

#Run simulation
def main():
    simulation()
    print("----------------------------------------------------")
    
    
    for i in range(4):
        answer = input("Would you like another reading? [Y]es or [N]o?: ")
        if answer == "Y" or answer == "y" or answer == "yes" or answer == "Yes":
            print("*************************************************")
            simulation()
            print("------------------------------------------------")
        else:
            print("              ***Farewell***                  ")
            return "end"

main()
