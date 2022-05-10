def main():
    # Ask user to enter a series of single-digit numbers
    # with nothing separating them
    numbers = input('Enter a series of numbers with nothing separating them: ')

    # Add an accumulator to keep sum
    sum = 0

    # Iterate through each number and add that number to the accumulator
    for num in numbers:
        sum += int(num)

    # Display the sum results
    print(f'Sum of numbers entered: {sum}')
    print()

# Call main function
main()
