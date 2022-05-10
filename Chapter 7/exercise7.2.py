# Global constants
DIGITS = 7

# Define main function
def main():
    # Import random module
    import random

    # Create list the length of DIGITS
    lotteryNum = [0] * DIGITS

    # Iterate through each element in the list by returning how many elements
    # are in the list to the range function
    for index in range(len(lotteryNum)):
        # Assign each element a random value 0-9
        lotteryNum[index] = random.randrange(10)

    # Iterate through the list lotteryNum
    for item in lotteryNum:
        # Display the items in the list
        print(item)

# Call the main function
main()
