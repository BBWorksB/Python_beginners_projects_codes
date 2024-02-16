#import libraries
import random
import math

#set the upper and lower bound
#Taking the inputes

upper = int(input("Enter upper bound:- "))
lower = int(input("Enter lower bound:- "))

#Generate random number between the lower and the upper bound
num = random.randint(lower, upper)

#Calculate the number of guess
#Will use this formula
#num of guessess = log2(upper - lower+1)
num_guesses = round(math.log(upper - lower +1,2 ))
print("\n\t You have", num_guesses ,
      "chances to guess the number")

# Count the guesses
count = 0

while count < math.log(upper - lower +1, 2):
    count += 1

    #Take the guess
    guess = int(input("Guess a number: "))

    # Check the number with condition
    if num == guess:
        print(f"Congratulations you woen!! After {count} trys.")

        # Break the loop once guess is made
        break
    elif num > guess:
        print("Your guess is too small")
    elif num < guess:
        print("Your guess is too high")

# If the guesses are more than required show the output
if count >= math.log(upper - lower+1, 2):
    print("\nThe number is %d" %num)
    print("\t Try again Next time!! You Loser!!")