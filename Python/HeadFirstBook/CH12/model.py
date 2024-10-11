#var for height and width values used to for the size of the grid
height = 100
width = 100

#multiply the list of zero by the value in height
grid_model = [0] * height

#iterate through the range of height and use it to multiply the 0 list by the width to make the grid
for i in range(height):
    grid_model[i] = [0] * width  

 #function for creating the next gen of cells 
def next_gen():
    global grid_model
   #iterate through the height and width of the grid using a nested loop
    for i in range(0, height):
        for j in range(0, width):
            cell = 0
            print('Checking cells', i, j)
            count = count_neighbors(grid_model, i, j)
            
            if grid_model[i][j] == 0:
                if count == 3:
                    cell = 1
            elif grid_model[i][j] == 1:
                if count == 2 or count == 3:
                    cell = 1
                

def count_neighbors(grid, row, col):
    
    count=0
    
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

if __name__ == '__main__':
    next_gen()
        
    