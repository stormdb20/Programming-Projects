#import Tkinter using a different method. Tkinter will make the window and the widgets for buttons
from tkinter import *
#Create our window being mindful of letter case and using the root var which is customary in coding
root = Tk()
#giving the window a title 
root.title('The Game Of Life')
#Give the window a button be careful of letter case passing it the button object a text, size, and what root it belongs to argument
start_button = Button(root, text='Start', width=12)
#A layout manager for the widgets which has Tkinter put the buttons whereever there is space
start_button.pack()
#Gives control of everything to Tkinter to manage and react to interaction with the window and widgets
mainloop()

