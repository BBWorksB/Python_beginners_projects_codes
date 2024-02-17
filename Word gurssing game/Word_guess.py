# import the random library
# the library helps in to choose random words from a list
import random
name = input("Tell us your name: ")
print(f"All the best {name.upper} as you crack the puzzle!!")

# The list of words
words = ['Baraka', 'Kamau', ' Faith', 'Jackson'
         'Car','Excellent', 'Amazing','Congratulations']

# Choose random word from the words
word = random.choice(words)

print("Suprise us with a character: ")

guesses = ' '
rounds = 10

while  rounds > 0:
    #count the number of failures
    fail = 0

    # Check the characters in the random word
    for char in word:
        #Check the char with the guesses
        if char in guesses:
            print(char, end=' ')
        else:
            print('__')
            #Increase the fail for every wrong guess
            fail += 1

    if fail == 0:
        # The user has won
        print("Hurreyyy!!! Winner!!")
        print(f"The word is, {word}")
        break

    # if the user has failed they will be asked to guess another character
    print()
    guess = input("Suprise us with a character: ")

    #Every guess will be stored in in guesses
    guesses += guess

    #Check the input with the character in word
    if guess not in word:
        rounds -= 1
        #if character not in word print wrong
        print("Wrong")

    #Print number of turns remaining
        print(f"You have  {rounds} guesses remaining.")

        if rounds == 0:
            print("YOU ARE A LOSER!!!")
