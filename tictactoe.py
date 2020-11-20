from tkinter import *

# Main frame for imported library
root= Tk()
root.geometry("290x258")

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

root.mainloop()