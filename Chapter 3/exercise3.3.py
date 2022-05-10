# Ask user for a person's age
age = int(input('Enter a person\'s age: '))

# Check age with ranges and display if the person is an infant, child,
# teenager, or adult
if age <= 1:
    print('This person is an infant.')
elif age > 1 and age < 13:
    print('This person is a child.')
elif age > 13 and age < 20:
    print('This person is a teenager.')
elif age > 20:
    print('This person is an adult.')
