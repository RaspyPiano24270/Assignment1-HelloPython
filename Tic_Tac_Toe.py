"""
-----------------------------------------------------------------------------
Name: Eric Gerner
Date: 9 June 2025
Course: Artificial Intelligence
-----------------------------------------------------------------------------
Simple Tic Tac Toe Game with Tkinter
-----------------------------------------------------------------------------
"""

#imports
from tkinter import *
import random

#functions
def nextTurn(row, column): #alternates between player 1 and 2 until either one of them wins or there's a draw
    global player
    if buttons[row][column]['text'] == "" and checkWin() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if checkWin() is False:
                player = players[1]
                label.config(text=(players[1]+"'s turn"))
            elif checkWin() is True:
                label.config(text=(players[0]+" is victorious"))
            elif checkWin() == "Tie":
                label.config(text=("Draw!!"))
        else:
            buttons[row][column]['text'] = player
            if checkWin() is False:
                player = players[0]
                label.config(text=(players[0]+"'s turn"))
            elif checkWin() is True:
                label.config(text=(players[1]+" is victorious"))
            elif checkWin() == "Tie":
                label.config(text=("Draw!!"))
def checkWin(): #checks if win conditions have been met, also adds colors to tiles that've been clicked on
    for row in range(3): #checks for 3 across
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="blue")
            buttons[row][1].config(bg="blue")
            buttons[row][2].config(bg="blue")
            return True
    for column in range(3): #checks for 3 down
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="blue")
            buttons[1][column].config(bg="blue")
            buttons[2][column].config(bg="blue")
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "": #checks for diagonal
        buttons[0][0].config(bg="blue")
        buttons[1][1].config(bg="blue")
        buttons[2][2].config(bg="blue")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "": #checks for other diagonal
        buttons[0][2].config(bg="blue")
        buttons[1][1].config(bg="blue")
        buttons[2][0].config(bg="blue")
        return True
    elif emptySpace() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="red")

        return "Tie"
    else:
        return False
def emptySpace(): #changes an empty space when clicked on to either x or o
    
    spaces = 9
    
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -=1
    if spaces == 0: #no more empty spaces + no win condition met = tie
        return False
    else:
        return True #means there is a winner
def newGame(): #clears the window before or after the game concludes and resets the game
    global player

    player = random.choice(players)
    label.config(text=player+"'s turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="white")

#create window: sets up the window, its labels, buttons, and appearance
window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"]
player = random.choice(players)
buttons = [[0,0,0],[0,0,0],[0,0,0]]
label = Label(text= player + "'s turn", font=('impact', 30))
label.pack(side="top")

resetButton = Button(text="clear", font=('impact', 10), command=newGame)
resetButton.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame,text="",font=('impact', 30,), width=6, height=3, 
                                    command= lambda row=row, column=column: nextTurn(row, column))
        buttons[row][column].grid(row=row, column=column)
window.mainloop()