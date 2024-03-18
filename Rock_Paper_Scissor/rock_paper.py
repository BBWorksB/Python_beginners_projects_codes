# We import random
import random

#print the commands
print('For you to win the game: \n'
      + "Rock vs Paper -> Paper Wins \n"
      + "Rock vs Scissors -> Rock Wins \n"
      + "Paper vs Scissors -> Scissors Wins \n")

while True:
    print("Enter your choice: \n 1 - Rock \n 2 - Paper \n 3 - Scissors\n")

    #Get the gamer input
    choice = int(input("Enter your Choice: "))


    # Check whether the input is the correct input
    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid choice master......: ")) 

    # initialize the choices
    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name == "Paper"
    else:
        choice_name == "Scissors"

    # Print the user choice
    print(f"Your choice is \n {choice_name}")
    print("Computer turn.........")

    #The comp choice
    comp_choice = random.randint(1,3)

    # loop to check if the comp choice is == to the choice
    while comp_choice == choice:
        comp_choice = random.randint(1,3)

    #initilise the comp choice options
    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissors"

    #Print computer choice
    print(f"The computer choice is \n {comp_choice_name}")

    # The choice
    print(f"Who is the winner!! \n{choice_name} vs {comp_choice_name}")


    #Conditions if its a draw or a win
    if choice == comp_choice:
        print("It's a DRAW", end="")
        result = "Draw"

    # Conditions for winning
    if choice == 1 and comp_choice == 2:
        print("Paper Wins")
        result = "PapeR"
    
    elif (choice==2 and comp_choice==1):
        print('paper wins =>',end="")
        result='Paper'
         
       
    if (choice==1 and comp_choice==3):
        print('Rock wins =>\n',end= "")
        result='Rock'
    elif (choice==3 and comp_choice==1):
        print('Rock wins =>\n',end= "")
        result='rocK'
         
    if (choice==2 and comp_choice==3):
        print('Scissors wins =>',end="")
        result='scissoR'
    elif (choice==3 and comp_choice==2):
        print('Scissors wins =>',end="")
        result='Rock'
     # Printing either user or computer wins or draw
    if result == 'DRAW':
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again? (Y/N)")
    # if user input n or N then condition is True
    ans = input().lower()
    if ans =='n':
        break
# after coming out of the while loop
# we print thanks for playing
print("thanks for playing")
            
        