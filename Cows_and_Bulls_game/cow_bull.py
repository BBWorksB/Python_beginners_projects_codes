# Game will use the random library
# The computer will generate a random 4 digit code
# The use will try to guess and it will print 
# numbe of bulls - the correct guess on the correct position
# number of cows - the correct guess onthe wrong position
# The secrete code should not be have a duplicate number

import random

#function to get the list of the digit
def digits(num):
    return [int(i) for i in str(num)]

# check if there is a duplicate
def duplicates(num):
    num_li = digits(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False
    
# Generate the secret code with no duplicates 
def secretcode():
    while True:
        num = random.randint(1000, 9999)
        if duplicates(num):
            return num
        
# return bulls and cows
def numBullCows(num, guess):
    bull_cow = [0,0]
    num_li = digits(num)
    guess_li = digits(guess)

    for i, j in zip(num_li,guess_li):
        #common digits present
        if j in num_li:
            #common digit exact match
            if j == i:
                bull_cow[0] += 1

            # Common digit wrong match
            else:
                bull_cow[1] += 1

    return bull_cow


# Secrete Code
num = secretcode()
tries = int(input("Enter number of tries: "))

# Play the game till there is correct guess or the tries are over
while tries > 0:
    guess = int(input("Enter your guess: "))

    if not duplicates(guess):
        print("Number should not have duplicates try again.")
        continue

    if guess < 1000 or guess > 9999:
        print("Enter a four digit number. Try again!")
        continue

    bull_cow = numBullCows(num, guess)
    print(f"{bull_cow[0]} Bulls, {bull_cow[1]} Cows")
    tries -= 1

    if bull_cow[0] == 4:
        print("You guessed right! \n YOU WINN!!")
        break
else:
    print(f"You ran out of tries. \n\n The number was {num}")