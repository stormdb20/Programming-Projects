#var for height and width values used to for the size of the grid
height=100
width=100

#multiply the list of zero by the value in height
grid_model=[0] * height

#iterate through the range of height and use it to multiply the 0 list by the width to make the grid
for i in range(height):
    grid_model[i]= 0 * width  

 #function for creating the next gen   
def next_gen():
    global grid_model
   #iterate through the height and width of the grid using a nested loop
    for i in range(0, height):
        for j in range(0, width):
            cell=0