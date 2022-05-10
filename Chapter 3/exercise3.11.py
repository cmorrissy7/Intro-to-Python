# Ask user for the number of books that they purchased this month
booksPurchased = int(input('Enter the number of books purchased this month: '))

# Calculate the points awarded by number of books purchased
if booksPurchased >= 0 and booksPurchased < 2: #if books purchased 0 or 1
    print('Points awarded: 0')
elif booksPurchased >= 2 and booksPurchased < 4:#if books purchased is 2 or 3
    print('Points awarded: 5')
elif booksPurchased >= 4 and booksPurchased < 6:#if books purchased is 4 or 5
    print('Points awarded: 15')
elif booksPurchased >= 6 and booksPurchased < 8:#if books purchased is 6 or 7
    print('Points awarded: 30')
elif booksPurchased >= 8:#if books purchased is 8 or more
    print('Points awarded: 60')
else:#if invalid entry
    print('Error')
