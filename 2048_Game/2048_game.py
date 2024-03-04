# Importing the gamecode that has all the functions of the game
import gamecode

if __name__ == '__main__':
    # Call the start game function
    mat = gamecode.startgame()

while (True):
    # Take the users commands
    command = input("What's your move? ")

    # if we move up
    if (command == "U" or command == "u"):

        # Call the move up function
        mat, flag = gamecode.move_up(mat)

        # Print the status of the game
        status = gamecode.game_state(mat)

        print(status)

        # If game not over continue and hold a new 2
        if status == "Game Not Over: CONTINUE SWAPPING!!":
            gamecode.add2(mat)

        #otherwise break the loop
        else:
            break

        #The same step is followed for any command

    # If we move down
    elif( command == "D" or command == 'd'):
        mat, flag = gamecode.move_down(mat)
        status = gamecode.game_state(mat)
        print(status)
        if status == "Game Not Over: CONTINUE SWAPPING!!":
            gamecode.add2(mat)
        else:
            break

    #If we move left
    elif(command == "L" or "l"):
        mat,flag = gamecode.move_left(mat)
        status = gamecode.game_state(mat)
        print(status)
        if status == "Game Not Over: CONTINUE SWAPPING!!":
            gamecode.add2(mat)
        else:
            break

    # If we move right
    elif(command == "R" or "r"):
        mat,flag = gamecode.move_right(mat)
        status = gamecode.game_state(mat)
        print(status)
        if status == "Game Not Over: CONTINUE SWAPPING!!":
            gamecode.add2(mat)
        else:
            break

    else:
        print("Invalid Command")

    # After each move print the matrix
    print(mat)