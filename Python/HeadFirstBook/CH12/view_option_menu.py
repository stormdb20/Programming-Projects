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
    
    clear_button = Button(root, text='Clear', width=12)
   
    #Stringvar object to hold multiple string values and use the proper one selected
    choice = StringVar(root)
    choice.set('Choose a Pattern')
    option = OptionMenu(root, choice,'Choose a Pattern', 'Glider', 'Glider Gun', 'Random', command=option_handler)
    option.config(width=20)
#A grid layout manager to specify the widgets location based off rows and columns
    grid_view.grid(row=0, columnspan=3, padx=20, pady=20)
    #bind the clicking of the left mouse button to the grid handler function
    grid_view.bind('<Button-1>', grid_handler)
    start_button.grid(row=1, column=0, sticky=W, padx=20, pady=20)
    #Event handler for start button which will give it reaction to being clicked
    start_button.bind('<Button-1>', start_handler)
    option.grid(row=1, column=1, padx=20)
    
    clear_button.grid(row=1, column=2, sticky=E, padx=20, pady=20)
    # event handler for the clear button
    clear_button.bind('<Button-1>', clear_handler)

#Function for option menu handler
def option_handler(event):
    global is_running, start_button, choice
    #Set is_running to false and make the start button display start as text
    is_running = False
    start_button.configure(text='Start')
    #var to hold the get method that is applied to the choice var holding the stringvar object value
    selection = choice.get()
    #compare and resolve based on the users option menu selection
    if selection == 'glider':
        model_random.load_pattern(model_random.glider_pattern, 10, 10)
    
    elif selection == 'glider gun':
        model_random.load_pattern(model_random.glider_gun_pattern, 10, 10)
    
    elif selection == 'random':
        model_random.randomize(model_random.grid_model, model_random.width, model_random.height)
    
    update()

        
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
    
#clear button handler to set is_running to false and iterate throught the cells making them zero then change start button text and call update
def clear_handler(event):
    global is_running, start_button
    is_running = False
    for i in range(0, model_random.height):
        for j in range(0, model_random.width):
            model_random.grid_model[i][j] = 0
    
    start_button.configure(text='Start')
    update()
#when left click on screen find cell position and invert whatever is there applying proper color for live or dead cell
def grid_handler(event):
    global grid_view,cell_size
    #get the x and y position of the cell and divide by cell size for accuracy
    x = int(event.x / cell_size)
    y = int(event.y / cell_size)
    #check id cell at position x,y is live. If it is make it dead with appropriate color
    if (model_random.grid_model[x][y] == 1):
        model_random.grid_model[x][y] = 0
        draw_cell(x, y, 'white')
    #make cell live and apply appropriate color    
    else:
        model_random.grid_model[x][y] = 1
        draw_cell(x, y, 'black')
       

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

