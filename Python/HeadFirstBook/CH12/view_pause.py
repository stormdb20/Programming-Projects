#import Tkinter using a different method. Tkinter will make the window and the widgets for buttons
from tkinter import *
#import model module i created
import model_random
#var for cell_size since we want the cell size bigger than a pixel
cell_size = 5
#var holding True or False depending on if our program is computing a next gen
is_running = False

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
    #Event handler for start button which will give it reaction to being clicked
    start_button.bind('<Button-1>', start_handler)
    clear_button = Button(root, text='Clear', width=12)
   # 
    choice = StringVar(root)
    choice.set('Choose a Pattern')
    option = OptionMenu(root, choice,'Choose a Pattern', 'Glider', 'Glider Gun', 'Random')
    option.config(width=20)
#A grid layout manager to specify the widgets location based off rows and columns
    grid_view.grid(row=0, columnspan=3, padx=20, pady=20)
    start_button.grid(row=1, column=0, sticky=W, padx=20, pady=20)
    option.grid(row=1, column=1, padx=20)
    clear_button.grid(row=1, column=2, sticky=E, padx=20, pady=20)

#start button handler function passed the event special argument to manipulate the start button 
def start_handler(event):
    global is_running, start_button
    #use is_running var to manipulate te text and behaviour of the start button into start/pause button and call update when start is clicked
    if is_running:
        is_running = False
        start_button.configure(text='Start')
    else:
        is_running = True
        start_button.configure(text='Pause')
        update()
    
    

#function to update the canvas with the next gen
def update():
    global grid_view, root, is_running
    #delete everything in the canvas
    grid_view.delete(ALL)
    #compute the next gen
    model_random.next_gen()
    #iterate through the cells and draw a rectangle with the color black if cell is live(1)
    for i in range(0, model_random.height):
        for j in range(0, model_random.width):
            if model_random.grid_model[i][j] == 1:
                draw_cell(i,j, 'black')
   #check if is_running currently true
    if (is_running):
        #if true then have root use the after method to call update after 100 milliseconds
        root.after(100, update)
#function to draw cell and color it also giving it an outline and shape
def draw_cell(row, col, color):
    global grid_view, cell_size
    #if/else statement to choose outline color 
    if color == 'black':
        outline = 'grey'
    else:
        outline = 'white'
    #create rectangle with color and outline color with upper left and bottom right coordinates
    grid_view.create_rectangle(row*cell_size,
                               col*cell_size,
                               row*cell_size+cell_size,
                               col*cell_size+cell_size,
                               fill=color, outline=outline)
    





#compare to see if in main program or not
if __name__ == '__main__':
#Call setup function to make window with buttons
    setup()
#Call update function to compute and display the next gen
    update()
#Gives control of everything to Tkinter to manage and react to interaction with the window and widgets
    mainloop()

