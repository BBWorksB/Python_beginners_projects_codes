# The game is going to be between the computer and you
# We will not use the pygame libraries
import random

# use randrange to generate a random number between the specified range
# Function to generate the random/secrect number
def generatenumber():
    num = random.randrange(1000, 1000)
    return num

#Player 1 guess the number
def guessnumber():
    while True:
        try:
            num = input("Guess the 4 digit number:")
            n = list(map(int, num.strip()))
            if len(n) == 4 and all(1<=digit <= 9 for digit in n):
                return num
            else:
                print("Please Enter four digits")
        except ValueError:
            print("Invalid input. Please enter 4 digits")
        
#Check the equality
def evaluate_guess(secret_code, guess):
    if secret_code == guess:
        print("MASTERMIND MASTER YOU ARE")
        print("You just guessed the number with one guess")
    
    else:
         tries = 0
         while secret_code != guess:
            tries += 1
            count = 0

            correct = ["X"]*4

            for i in range(0,4):
                if secret_code[i] == guess[i]:
                    count += 1
                    correct[i] = guess[i]
                else:
                    continue
            if count == 4:
                print("\nCongratulations!!")
                print(f"\n It took you {tries} to get it right.")  
                break
            else:
                print(f"Not the number but you got {count} correct.")
                print("\n\n")
                guess = int(input("Please Enter your next choice of numbers: "))
    if secret_code == guess:
        tries += 1
        print("Congratulations")

#play the game
def mastergame():
    print("Lets Play the game")
    print("Guess the secret code of four digits.")
    secretcode = generatenumber()
    
    
# #Condition to check the equality of the random and the guessed number
# #Terminate if its true
# if n == num:
# else:
#     # Store the number of tries the player tries
#     tries = 0
#     #use the while loop to keep the count 
#     while n != num:
#         tries += 1
#         count = 0
#         #Convert the int to string for easy extraction of digits
#         n = str(n)
#         num = str(num)
#         # Store the correct intergers
#         correct = ['X']*4
#         # For loop should run 4 times since there are 4 digits
#         for i in range(0,4):
#             #check equality of the digits
#             if n[i] == num[i]:
#                 #count the number of digits guessed correctly
#                 count += 1
#                 #strore the digits in correct
#                 correct[i] = n[i]
#             else:
#                 continue
#         # Print the feedback
#         if count == 4:
#             print("\nCongratulations!!")
#             print(f"\n It took you {tries} to get it right.")
#             break
#         else:
#             print(f"Not the number but you got {count} correct.")
#             print("\n\n")
#             n = int(input("Please Enter your next choice of numbers: "))

#     # condition for equality
#     if n == num:
#         tries += 1
#         print("Congratulations!!!")

