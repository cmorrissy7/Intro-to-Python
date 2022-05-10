#Ask user for a number in the range of 1-7
number = int(input('Number between 1 and 7: '))

#Print corresponding day of the week with the number
#or print error message if the number is outside the range
if number == 1:
    print('Monday')
elif number == 2:
    print('Tuesday')
elif number == 3:
    print('Wednesday')
elif number == 4:
    print('Thursday')
elif number == 5:
    print('Friday')
elif number == 6:
    print('Saturday')
elif number == 7:
    print('Sunday')
else:
    print('Error: Number outside the range of 1-7')
