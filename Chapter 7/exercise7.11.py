# Define function to accept a 2D list and checks if it is a
# Lo Shu Magic Square
def isMagic(twoList):
    if twoList[0][0] + twoList[0][1] + twoList[0][2] == 15\
       and twoList[1][0] + twoList[1][1] + twoList[1][2] == 15\
       and twoList[2][0] + twoList[2][1] + twoList[2][2] == 15\
       and twoList[2][0] + twoList[1][1] + twoList[0][2] == 15\
       and twoList[0][0] + twoList[1][1] + twoList[2][2] == 15\
       and twoList[0][0] + twoList[1][0] + twoList[2][0] == 15\
       and twoList[0][1] + twoList[1][1] + twoList[2][1] == 15\
       and twoList[0][2] + twoList[1][2] + twoList[2][2] == 15:
        return True
    else:
        return False

# Define main function that will hold good and bad (magic or not magic) squares
# and iterates through them to test them with the isMagic function
def main():
    # Create list of known good squares (magic) for viewing purposes
    goodSquares = [[[4, 9, 2], [3, 5, 7], [8, 1, 6]],
                  [[8, 3, 4], [1, 5, 9], [6, 7, 2]]]

    # Create list of known bad squares (not magic) for viewing purposes
    badSquares = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]

    # Create list of all squares so it can be used to test the isMagic function
    allSquares = goodSquares + badSquares
    
    # Use a for loop to go through each square and call the isMagic function
    for index in allSquares:
        # This displays the list being tested
        print(f'List being tested: {index}')

        # Calls isMagic function to test if list is magic square
        # and displays if it is or is not to the user
        if isMagic(index):
            print('This list is a Lo Shu Magic Square!\n')
        else:
            print('This list is not a Lo Shu Magic Square.\n')

    # Once the for loop has finished executing, the program should display
    # that the first two squares are magic, and the next two are not magic

# Call the main function if running program
if __name__ == "__main__":
    main()
