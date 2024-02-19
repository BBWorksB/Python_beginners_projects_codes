#Import libraries
import random
from collections import Counter

words = "banana orange apple mango tomato pineapple lemon watermelon cherry"
words = words.split(" ")

#select random words
word = random.choice(words)

if __name__ == "__main__":
    name = input("Whats your NAME:")
    print(f"Your turn {name} to guess a name(Hint: Fruits)")

    for i in word:
        # Print empty blanks for the letters of the word chosen ranomly
        print("_", end= ' ')
    print()

    playing = True
    #Store the letters guessed
    lettersguessed = ""
    chances = len(word)+2
    #Chances the player has to guess the letters
    correct = 0
    flag = 0
    # Flag is updated when the letter guessed is correct

    try:
        while (chances !=0 ) and flag == 0:
            print()
            chances -= 1

            # Guess the letter and it must be a letter
            try:
                guess = str(input("Guess a letter for the word: "))
            except:
                print("Enter only a letter!!")
                continue

            #validate the guess
            if not guess.isalpha(): #check the guess if its an alphabet
                print("Enter only Letters!!")
                continue
            elif len(guess) > 1:
                print("Enter only a SINGLE letter")
                continue
            elif guess in lettersguessed:
                print("You have already guessed that letter")
                continue

            # If the letter guessed is correct
            if guess in word:
                # k stores the number of times the guess letters occurs in the word
                #the guessed letter is added as many times as its occurance
                k = word.count(guess)
                for _ in range(k):
                    lettersguessed += guess

            # Print the word
            for char in word:
                if char in lettersguessed and (Counter(lettersguessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                 #If the player has guessed all letters
                 # Once the final correct guesed letter is keyed
                    
                elif (Counter(lettersguessed) == Counter(word)):
                    #The game ends
                    print(f"The word is: {word}", end=' ')
                    flag = 1
                    print("\n\tCongratulations you Won!!")
                    break # out of the for loop
                    break #out of the while loop
                else:
                    print("_", end=" ")
        
        # If user has used all the chances
        if chances <= 0 and (Counter(lettersguessed) != Counter(word)):
            print()
            print("You lost FAILURE!!")
            print(f"The word was {word}")
    
    except KeyboardInterrupt:
        print()
        print("Bye try again!!")
        exit()