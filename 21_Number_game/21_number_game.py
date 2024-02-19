# Return the multiple of four
def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near

# The lose function
def lose1():
    print("\n YOU LOOOOOOOOOOOSEEE!!!")
    print("Better try next time!")
    exit(0)

# Check if the number are consecutive
def check(xyz):
    i = 1
    while i < len(xyz):
        if (xyz[i] - xyz[i-1]) != 1:
            return False
        i = i + 1
    return True

# Start the game
def start1():
    xyz = []
    last = 0
    while True:
        print("Enter 'F' to take the first chance: ")
        print("Enter 'S' to take the second chance: ")
        chance = input("> ")

        # Player takes the first chance
        if chance == "F":
            while True:
                if last == 20:
                    lose1()
                else:
                    print("\n Your Turn!!")
                    print("How many numbers do you wish to enter?")
                    inp = int(input("> "))

                    if inp > 0 and inp <= 3:
                        comp = 4 - inp
                    else:
                        print("Wrong input. You are disqulified try again next time.")
                        lose1()
                    
                    i, j = 1, 1

                    print("Now enter the values: ")
                    while i <= inp:
                        a = int(input("> "))
                        xyz.append(a)
                        i = i + 1

                    #Store the last element of xyz
                    last = xyz[-1]


                    # Check wether the input numbers are consecutive
                    if check(xyz) == True:
                        if last == 21:
                            lose1()

                        else:
                            # The computers turn
                            while j <= comp:
                                xyz.append(last + j)
                                j = j + 1
                            print("Order of input is: ")
                            print(xyz)
                            last = xyz[-1]
                    
                    else:
                        print("\n You did not input consecutive integers.")
                        lose1()

        # Player takes second chance
        elif chance == "S":
            comp = 1
            last = 0
            while last < 20:
                # Computers turn
                j = 1
                while j <= comp:
                    xyz.append(last + j)
                    j = j + 1
                print("Order of inputs is: ")
                print(xyz)
                if xyz[-1] == 20:
                    lose1()

                # Your turn
                else:
                    print("\n Your Turn")
                    print("\n How many numbers do you want to enter?")
                    inp = int(input("> "))

                    i = 1
                    print("Enter your values: ")
                    while i <= inp:
                        xyz.append(int(input("> ")))
                        i = i + 1
                    last = xyz[-1]

                    if check(xyz) == True:
                        # print xyz
                        near = nearestMultiple(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3

                        else:
                            comp = comp
                    
                    else:
                        # If numbers are not consecutive you lose
                        print("\n You didn't key in consecutive integers!!")
                        lose1()
            print("\n Congratualtions you Won!!")
            exit(0)
        
        else:
            print("\n Wrong Choice!!")

game = True
while game == True:
    print("Player 2 is Computer")
    print("Do you want to play the 21 number game? (Yes/No)")
    ans = input("> ")
    if ans == "Yes":
        start1()
    else:
        print("Do you want to quit?(Yes/No)")
        nex = input("> ")
        if nex == "yes":
            print("You are quiting the game....")
            exit(0)
        elif nex == "no":
            print("Continueing....")
        else:
            print("Wrong Choice")