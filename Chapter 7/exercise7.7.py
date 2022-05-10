# Global constants
PASS_GRADE = 15
TOTAL_QUESTIONS = 20

# Create a list of correct answers
correctAnswers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
           'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

def main():
    # Local variables
    totalCorrect = 0
    totalIncorrect = 0
    
    # Open the student's answer file
    infile = open('student_answers.txt', 'r')

    # Read the contents into a list
    studentAnswers = infile.readlines()

    # Close the file
    infile.close()

    # Strip the \n from each element
    for index in range(len(studentAnswers)):
        studentAnswers[index] = studentAnswers[index].rstrip('\n')

    # Create list for incorrect answers
    incorrectAnswers = []

    # Iterate for each question
    for index in range(TOTAL_QUESTIONS):
        # Check if the answers are the same in both lists
        if correctAnswers[index] == studentAnswers[index]:
             # Add one to the total of correct
             totalCorrect += 1
        else:
            # Add one to the total of incorrect
            totalIncorrect += 1
            # Append the index of question to incorrect answer list
            incorrectAnswers.append(index)

    # If they have at least 15 correct answers
    if totalCorrect >= 15:
        # Print message indicating they passed
        print('You passed!')
    else:
        # Print message indicating they failed
        print('You failed.')

    # Display total correct, total incorrect, and the list of
    # questions that were incorrect
    print(f'Total correct: {totalCorrect}')
    print(f'Total incorrect: {totalIncorrect}')
    print('Here are the quesions you got wrong:')

    for index in range(len(incorrectAnswers)):
        print(incorrectAnswers[index] + 1)

# Call main function
main()
