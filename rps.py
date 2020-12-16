from tkinter import *
from random import randint

win = 'YOU WIN!'
lose = 'YOU LOSE!'
tie = 'ITS A DRAW!'


#Creating a random number generator that creates the computer's choice
def numGen():
    value = randint(0,2)
    return(value)

#Comparing the computer's chouce with the player's choice
def compareWithComputer(playerInt):
    compInt = numGen()
    if(compInt == 0):
        if(playerInt == 0):
            return tie
        
        elif (playerInt == 1):
            return win
        
        else:
            return lose

    elif(compInt == 1):
        if(playerInt == 0):
            return lose
        
        elif (playerInt == 1):
            return tie
        
        else:
            return win
    
    else:
        if(playerInt == 0):
            return win
        
        elif (playerInt == 1):
            return lose
        
        else:
            return tie
        
#Creating the methods for the different buttons
def selectRock():
    responceLbl['text'] = compareWithComputer(0)
    
def selectPaper():
    responceLbl['text'] = compareWithComputer(1)

def selectScissors():
    responceLbl['text'] = compareWithComputer(2)


#Creating the GUI using Tkinter
root = Tk()

#Creating variables that hold the icons
rockImg = PhotoImage(file = r"C:\Users\adity\Documents\GitHub\RockPaperScissors\icons\rock.png")
paperImg = PhotoImage(file = r"C:\Users\adity\Documents\GitHub\RockPaperScissors\icons\paper.png")
scissorsImg = PhotoImage(file = r"C:\Users\adity\Documents\GitHub\RockPaperScissors\icons\scissors.png")

titleLbl = Label(root, text='Rock Paper Scissors!')
promptLbl = Label(root, text='click a button')
rockBtn = Button(root, text='  rock   ', padx=20, pady=7, bg='light blue', command=selectRock, image=rockImg, compound=RIGHT)
paperBtn = Button(root, text='  paper ' , padx=20, pady=7, bg='light green', command=selectPaper, image=paperImg, compound=RIGHT)
scissorsBtn = Button(root, text='scissors', padx=25, pady=7, bg='pink', command=selectScissors, image=scissorsImg, compound=RIGHT)
responceLbl = Label(root)

titleLbl.pack()
promptLbl.pack()
rockBtn.pack()
paperBtn.pack()
scissorsBtn.pack()
responceLbl.pack()

root.mainloop()