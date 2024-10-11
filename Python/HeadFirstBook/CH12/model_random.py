#import random module
import random

    
#var for height and width values used to for the size of the grid
height = 100
width = 100

#function to randomize the values of the cells between live(1) and dead(2)
def randomize(grid, width, height):
    for i in range(0, height):
        for j in range(0, width):
            grid[i][j] = random.randint(0,1)
            
#multiply the list of zero by the value in height to make current and next gen grid models
grid_model = [0] * height
next_grid_model = [0] * height
#iterate through the range of height and use it to multiply the 0 list by the width to complete the current and next grid models
for i in range(height):
    grid_model[i] = [0] * width  
    next_grid_model[i] = [1] * width

#call the randomize function passing grid model, height, and width
#randomize(grid_model, width, height)
 
 #function for creating the next gen of cells 
def next_gen():
    global grid_model, next_grid_model
   #iterate through the height and width of the grid using a nested loop
    for i in range(0, height):
        for j in range(0, width):
            cell = 0
            #print('Checking cells', i, j)
            count = count_neighbors(grid_model, i, j)
            #compare whats in the grid position with the neighbor count to make it live(1) or dead(0)
            if grid_model[i][j] == 0:
                if count == 3:
                    cell = 1
            elif grid_model[i][j] == 1:
                if count == 2 or count == 3:
                    cell = 1
            #after cell completed store in the proper cell
            next_grid_model[i][j] = cell    
            #print('New value is', next_grid_model[i][j])
#makes the next grid model the current
    temp = grid_model
    grid_model = next_grid_model
    next_grid_model = temp

#function to count neighbors of each cell including the edges passing it grid row col
def count_neighbors(grid, row, col):
    
    count = 0
    #comparisons of the surrounding cells of the the current grid positions and increment the count of neighbors depending on reuslts
    if row-1 >= 0:
        count = count + grid[row-1][col]
        
    if (row-1 >=0) and (col-1 >=0):
        count= count + grid[row-1][col-1]
        
    if (row-1 >=0) and (col+1 < width):
        count= count + grid[row-1][col+1]
        
    if col-1 >= 0:
        count = count + grid[row][col-1]
        
    if col + 1 < width:
        count = count + grid[row][col+1]
        
    if row + 1 < height:
        count = count + grid[row+1][col]
    
    if (row + 1 < height) and (col-1 >= 0):
        count = count+ grid[row+1][col-1]
        
    if (row + 1 < height) and (col + 1 < width):
        count = count + grid[row+1][col+1]
        
    return count

glider_pattern = [[0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 0, 1, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0]]

glider_gun_pattern = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#Function to load patterns into the canvas passing vars and offset values for x and y to position pattern in canvas
def load_pattern(pattern, x_offset=0, y_offset=0):
    global grid_model
    #zero the cells
    for i in range(0, height):
        for j in range(0, width):
            grid_model[i][j] = 0
    #make j hold the offset value for y
    j = y_offset
    #itterate through the pattern placing 1's at the positions that match the position in canvas and make i the x offset 
    for row in pattern:
        i = x_offset
        for value in row:
            grid_model[i][j] = value
            i = i + 1
        j = j + 1

#comapre if program is in main or not and run the next gen function if it is
if __name__ == '__main__':
    next_gen()
        
    