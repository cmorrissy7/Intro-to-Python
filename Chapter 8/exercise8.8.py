# This program asks a user to enter a string, capitalizes every sentence,
# and then displays the modified string

# Define main function
def main():
    # Ask user for a string with sentences 
    string = input('Enter a string with sentences to be capitalized: ')
    
    # Call the capitalize_sentences function and pass the string the user
    # entered as an argument and return the results to the list "s_list"
    new_list = capitalize_sentences(string)

    # Display the new string by joining the list
    print('Here is the modified string:')
    print('. '.join(new_list))
    
# Define function that capitalizes the first letter of each sentence
def capitalize_sentences(string):
    # Split each sentence into tokens in the list "sentence_list"
    sentence_list = string.split('. ')

    # Create an empty list for modified sentences
    new_list = []

    # Iterate through each token in list
    for sentence in sentence_list:
        # Capitalize first letter of sentence
        new_sentence = sentence[0].upper()
        new_sentence += sentence[1:]

        # Append the new sentence to the s_list list
        new_list.append(new_sentence)

    # Return new_list
    return new_list

# Call the main function
if __name__ == '__main__':
    main()
