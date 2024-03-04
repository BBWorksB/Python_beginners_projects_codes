# This file has all the reasoning or rather the logics behind the 2048 game
# It will be imported to the 2048_game

# Will need random package to generate the random numbers
import random

# Function to a new 2 randomly to the grid
def add2(mat):

    # select a random index for row and column
    r = random.randint(0,3)
    c = random.randint(0,3)

    # A while loop will break as the random cells will contain
    # a zero or will be empty
    while mat[r][c] != 0:
        print("The value of r", r)
        r = random.randint(0,3)
        c = random.randint(0,3)

    # place a 2 at that random empty cell
    mat[r][c] = 2
    return mat
    
#Function to play the game
def startgame():
    # Creat a matrix by creating an empty list
    # Then we append 4 empty lists with 0 in it
    mat = []
    for i in range(4):
        mat.append([0] * 4)


    print("The value of mat", mat)

    # Defing the users controls
    print("The game commands are:")
    print("U or u to Move up.")
    print("D or d to Move down")
    print("L or l to Move Left")
    print("R or r to Move Right")

    #Call the function to add a 2 in the grid after every step
    add2(mat)
    print("The value of mat", mat)
    return mat



# Function to print out the current view or state of the game
def game_state(mat):

    # If any cell has 2048 then you win
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return "YOU WON!!"
            
    # Conditions when the game is not over
    # Print "Game is not over!!"
    # 1. When we have any empty cell
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return "Game Not Over: CONTINUE SWAPPING!!"
            
    # 2. We dont have any empty cell but when swapped two cells merge and create an empty cell.
    for i in range(3):
        for j in range(3):
            if (mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]):
                return "Game Not Over: CONTINUE SWAPPING!!"
            
    for j in range(3):
        if mat([3][j] == mat[3][j+1]):
            return "Game Not Over: CONTINUE SWAPPING!!"
        
    for i in range(3):
        if mat([i][3] == mat[i+1][3]):
            return "Game Not Over: CONTINUE SWAPPING!!"
        
    # If none of the conditions are satisfied return Game Over
    return "GAME OVER!!. You Lost!!"

# Will define a function for one swap{Left}
# Also a function to define the compressed grid after every swap before 
# and after merging the cells.
def compress(mat):

    # bool varible to check if there is any change
    change = False

    #New empty grid
    new_mat = []

    # With all cells empty
    for i in range(4):
        new_mat.append([0]*4)

    # Will shift entries for each to its extreme left row by row loop to traverse rows
    for i in range(4):
        pos = 0

        # Loop to traverse each column in respective row
        for j in range(4):
            if (mat[i][j] != 0):
            
            #If the cell is none empty then we will its number to the previous empty cell
            # in the row denoted by pos variable
             new_mat[i][pos] == mat[i][j]

             if j != pos:
                 change = True
            pos += 1
    
    # Return the compressed mat and the flagged variable
    return new_mat, change

# After compressing will need to merge the matrix cells
def merge(mat):
    changed = False

    for i in range(4):
        for j in range(3):

            #if current cell has the same value as the next cell in the row and they are non empty then
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:

                #double current cell value and empty the next cell
                mat[i][j] = mat[i][j]*2
                mat[i][j+1] = 0

                # Indicate a chenge was made by making the bool to be true
                changed = True
    
    return mat, changed

# Function to reverse the matrix reverseing th content of each row
def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3-j])
    return new_mat

# Transpose the matrix that is interchanging rows and columns
def transpose(mat):
    new_mat =[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat

# Update the matrix if we swipe left
def move_left(grid):

    # Compress the grid
    new_grid, changed1 = compress(grid)
    #Merge the cells
    new_grid, changed2 = merge(grid)
    changed = changed1 or changed2

    # Again compress after merging
    new_grid, temp = compress(new_grid)

    # Return the new matrix and bool change to know whether its the same or it changed
    return new_grid, changed

# Function when we move right, we need to reverse the mat and apply the left, then reverse it again
def move_right(grid):
    new_grid = reverse(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = reverse(new_grid)

    return new_grid, changed

# Function when we move up we just need to transpose the matrix, then apply the move left, then transpose back
def move_up(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = transpose(new_grid)

    return new_grid, changed

# Function when we move down/ swipe down, we transpose apply right move then transpose
def move_down(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_right(new_grid)
    new_grid = transpose(new_grid)

    return new_grid, changed
