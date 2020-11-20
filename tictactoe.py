from tkinter import *

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
    if box == 1 and player == 1:
        button1.config(text="O")
        player = 2
        bx1="O"


root.mainloop()