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
            return 'computer played rock: ' + tie
        
        elif (playerInt == 1):
            return 'computer played rock: ' + win
        
        else:
            return 'computer played rock: ' + lose

    elif(compInt == 1):
        if(playerInt == 0):
            return 'computer played paper: ' + lose
        
        elif (playerInt == 1):
            return 'computer played paper: ' + tie
        
        else:
            return 'computer played paper: ' + win
    
    else:
        if(playerInt == 0):
            return 'computer played scissors: ' + win
        
        elif (playerInt == 1):
            return 'computer played scissors: ' + lose
        
        else:
            return 'computer played scissors: ' + tie
        
#Creating the methods for the different buttons
def selectRock():
    responceLbl['text'] = compareWithComputer(0)
    
def selectPaper():
    responceLbl['text'] = compareWithComputer(1)

def selectScissors():
    responceLbl['text'] = compareWithComputer(2)


#Creating the GUI using Tkinter
root = Tk()
root.title("Rock Paper Scissors")
root.geometry("450x375")

#Creating variables that hold the icons
rockImg = PhotoImage(file = r"C:\Users\adity\Documents\GitHub\RockPaperScissors\icons\rock.png")
paperImg = PhotoImage(file = r"C:\Users\adity\Documents\GitHub\RockPaperScissors\icons\paper.png")
scissorsImg = PhotoImage(file = r"C:\Users\adity\Documents\GitHub\RockPaperScissors\icons\scissors.png")

titleLbl = Label(root, text='Rock Paper Scissors!', font=('anson', 25), padx=20, pady=10)
promptLbl = Label(root, text='click a button')
rockBtn = Button(root, text='  Rock   ', padx=20, pady=7, bg='light blue', command=selectRock, image=rockImg, compound=RIGHT)
paperBtn = Button(root, text='  Paper ' , padx=20, pady=7, bg='light green', command=selectPaper, image=paperImg, compound=RIGHT)
scissorsBtn = Button(root, text='Scissors', padx=25, pady=12, bg='pink', command=selectScissors, image=scissorsImg, compound=RIGHT)
responceLbl = Label(root, font=('roboto', 14), pady=5)

titleLbl.pack()
promptLbl.pack()
rockBtn.pack()
paperBtn.pack()
scissorsBtn.pack()
responceLbl.pack()

root.mainloop()