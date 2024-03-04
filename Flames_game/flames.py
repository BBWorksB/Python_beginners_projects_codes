# In the game we need to have to players
# they input their name and if there is a present similar letters they are dropped
# and count the remaining letters, then FLAMES is counted starting from F the last letter of the count is drooped
# and the next count starts from the next letter

# Define a function to check the and remove repeated occurances
def remove_match(input1, input2):
    for i in range(len(input1)):
        for j in range(len(input2)):

            # Remove common character
            if input1[i] == input2[j]:
                x = input1[i]

                # Remove character from the list
                input1.remove(x)
                input2.remove(x)

                list1 = input1 + ["*"] + input2

                return [list1, True]
            
# If no common character return  the list concantinated
    list1 = input1 + ["*"] + input2
    return [list1, False]

# Lets play the game
if __name__ == "__main__":
    input1 = input("Player 1 name: ")
    input1 = input1.lower()
    #if there is any space replace it wiht an empty string
    input1.replace(" ", "")
    #Make a list of the input or characters
    input1_list = list(input1)


    #Take the second name
    input2 = input("Player 2 name: ")
    input2 = input2.lower()
    input2.replace(" ","")
    input2_list = list(input2)

    #Declare the flag as true initislly 
    proceed = True

    # loop through the remove match function until comon character is found
    while proceed:
        # call and store the valuee
        ret_list = remove_match(input1_list, input2_list)

        # take out and concantinate the return list
        con_list = ret_list[0]

        # Take the flag output
        proceed = ret_list[1]

        # find the border mark "*" index
        bord_index = con_list.index("*")

        # list slicing 
        # all characters before *
        input1_list = con_list[: bord_index]
        # characters after
        input2_list = con_list[bord_index + 1: ]

    #count remaining characters
    count = len(input1_list) + len(input2_list)

    #List of the FLAMES
    results = ["Freinds", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    # Keep looping untiil one item is not remaining in the result list
    while len(results) > 1:

        split_index = (count % len(results)-1)
        if split_index >= 0:
            #slice the list
            right = results[split_index+1:]
            left = results[:split_index]

            #Slice concantination
            results = right + left

        else:
            results = results[: len(results) - 1]

    print("Relationship status : ", results[0])

