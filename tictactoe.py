# I have no idea why next line did not import all, but I had to import messagebox seperatelly to work
from tkinter import *
from tkinter import messagebox

# Main frame for imported library
root= Tk()
root.geometry("290x258")

# Values for the all game fields
bx1 = "1"
bx2 = "2"
bx3 = "3"
bx4 = "4"
bx5 = "5"
bx6 = "6"
bx7 = "7"
bx8 = "8"
bx9 = "9"

# Buttons for all game fields
button1 = Button(root, text = "  ",command = lambda: activate(1))
button1.grid(row='0',column="0",ipadx="40",ipady="30")
button2 = Button(root, text = "  ",command = lambda: activate(2))
button2.grid(row='0',column="1",ipadx="40",ipady="30")
button3 = Button(root, text = "  ",command = lambda: activate(3))
button3.grid(row='0',column="2",ipadx="40",ipady="30")
button4 = Button(root, text = "  ",command = lambda: activate(4))
button4.grid(row='1',column="0",ipadx="40",ipady="30")
button5 = Button(root, text = "  ",command = lambda: activate(5))
button5.grid(row='1',column="1",ipadx="40",ipady="30")
button6 = Button(root, text = "  ",command = lambda: activate(6))
button6.grid(row='1',column="2",ipadx="40",ipady="30")
button7 = Button(root, text = "  ",command = lambda: activate(7))
button7.grid(row='2',column="0",ipadx="40",ipady="30")
button8 = Button(root, text = "  ",command = lambda: activate(8))
button8.grid(row='2',column="1",ipadx="40",ipady="30")
button9 = Button(root, text = "  ",command = lambda: activate(9))
button9.grid(row='2',column="2",ipadx="40",ipady="30")

# Main game logic function and needed variables
player = 1
def activate(box):
    global player
    global bx1
    global bx2
    global bx3
    global bx4
    global bx5
    global bx6
    global bx7
    global bx8
    global bx9
    if box == 1 and player == 1:
        button1.config(text="O")
        player = 2
        bx1="O"
    elif box == 1 and player == 2:
        button1.config(text="X")
        player =1
        bx1="X"
    elif box == 2 and player == 1:
        button2.config(text="O")
        player = 2
        bx2="O"
    elif box == 2 and player == 2:
        button2.config(text="X")
        player =1
        bx2="X"
    elif box == 3 and player == 1:
        button3.config(text="O")
        player = 2
        bx3="O"
    elif box == 3 and player == 2:
        button3.config(text="X")
        player =1
        bx3="X"
    elif box == 4 and player == 1:
        button4.config(text="O")
        player = 2
        bx4="O"
    elif box == 4 and player == 2:
        button4.config(text="X")
        player =1
        bx4="X"
    elif box == 5 and player == 1:
        button5.config(text="O")
        player = 2
        bx5="O"
    elif box == 5 and player == 2:
        button5.config(text="X")
        player =1
        bx5="X"
    elif box == 6 and player == 1:
        button6.config(text="O")
        player = 2
        bx6="O"
    elif box == 6 and player == 2:
        button6.config(text="X")
        player =1
        bx6="X"
    elif box == 7 and player == 1:
        button7.config(text="O")
        player = 2
        bx7="O"
    elif box == 7 and player == 2:
        button7.config(text="X")
        player =1
        bx7="X"
    elif box == 8 and player == 1:
        button8.config(text="O")
        player = 2
        bx8="O"
    elif box == 8 and player == 2:
        button8.config(text="X")
        player =1
        bx8="X"
    elif box == 9 and player == 1:
        button9.config(text="O")
        player = 2
        bx9="O"
    elif box == 9 and player == 2:
        button9.config(text="X")
        player =1
        bx9="X"

# Winning condition - Rows
    if bx1 == bx2 == bx3 =="O" or bx4 == bx5 == bx6 =="O" or bx7 == bx8 == bx9 =="O":
        player = "O"
        messagebox._show("Game end", "player: " + player + " wins")
        exit(0)
    elif bx1 == bx2 == bx3 =="X" or bx4 == bx5 == bx6 =="X" or bx7 == bx8 == bx9 =="X":
        player = "X"
        messagebox._show("Game end", "player: " + player + " wins")
        exit(0)

# Winning condition - Columns
    elif bx1 == bx4 == bx7 =="O" or bx2 == bx5 == bx8 =="O" or bx3 == bx6 == bx9 =="O":
        player = "O"
        messagebox._show("Game end", "player: " + player + " wins")
        exit(0)
    elif bx1 == bx4 == bx7 =="X" or bx2 == bx5 == bx8 =="X" or bx3 == bx6 == bx9 =="X":
        player = "X"
        messagebox._show("Game end", "player: " + player + " wins")
        exit(0)

# Winning condition - Diagonals
    elif bx1 == bx5 == bx9 =="O" or bx3 == bx5 == bx7 =="O":
        player = "O"
        messagebox._show("Game end", "player: " + player + " wins")
        exit(0)
    elif bx1 == bx5 == bx9 =="X" or bx3 == bx5 == bx7 =="X":
        player = "X"
        messagebox._show("Game end", "player: " + player + " wins")
        exit(0)

root.mainloop()