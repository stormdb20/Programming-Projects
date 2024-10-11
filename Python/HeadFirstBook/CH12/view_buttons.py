#import Tkinter using a different method. Tkinter will make the window and the widgets for buttons
from tkinter import *
#import model module i created
import model_random
#var for cell_size since we want the cell size bigger than a pixel
cell_size = 5
#functio to create our buttons and put them into the window and also set the attributes of the buttons and window
def setup():
#Call in the global variables
    global root, grid_view, cell_size, start_button, clear_button, choice

#Create our window being mindful of letter case and using the root var which is customary in coding
    root = Tk()
#giving the window a title 
    root.title('The Game Of Life')
#Make a canvas widget passing multiple arguments to set the attributes of the canvas
    grid_view = Canvas(root, width=model_random.width*cell_size,
                       height=model_random.height*cell_size,
                       borderwidth=0,
                       highlightthickness=0,
                       bg='white')
#Give the window Buttons be careful of letter case passing it the button object a text, size, and what root it belongs to argument
    start_button = Button(root, text='Start', width=12)
    clear_button = Button(root, text='Clear', width=12)
   # 
    choice = StringVar(root)
    choice.set('Choose a Pattern')
    option = OptionMenu(root, choice,'Choose a Pattern', 'Glider', 'Glider Gun', 'Random')
    option.config(width=20)
#A layout manager for the widgets which has Tkinter put the buttons whereever there is space
    grid_view.pack()
    start_button.pack()
    option.pack()
    clear_button.pack()

#compare to see if in main program or not
if __name__ == '__main__':
#Call setup function to make window with buttons
    setup()
#Gives control of everything to Tkinter to manage and react to interaction with the window and widgets
    mainloop()

