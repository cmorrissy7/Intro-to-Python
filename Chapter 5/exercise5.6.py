# Global Constants
CALORIES_FROM_FAT = 9
CALORIES_FROM_CARBS = 4

# Define main function to control logic flow
def main():
    gramsFat = getFat()
    gramsCarbs = getCarbs()
    caloriesFat = setFat(gramsFat)
    caloriesCarbs = setCarbs(gramsCarbs)
    showCarbs(gramsFat, gramsCarbs, caloriesFat, caloriesCarbs)

# Function to get grams of fat consumed by user
def getFat():
    gramsFat = int(input('Grams of fat consumed in a day: '))
    return gramsFat

# Function to get grams of carbs consumed by user
def getCarbs():
    gramsCarbs = int(input('Grams of carbohydrates consumed in a day: '))
    return gramsCarbs

# Function to calculate the calories from fat
def setFat(gramsFat):
    caloriesFat = gramsFat * CALORIES_FROM_FAT
    return caloriesFat

# Function to calculate the calories from carbs
def setCarbs(gramsCarbs):
    caloriesCarbs = gramsCarbs * CALORIES_FROM_CARBS
    return caloriesCarbs

# Function to display grams and calories of fat and carbs consumed
def showCarbs(gramsFat, gramsCarbs, caloriesFat, caloriesCarbs):
    print(f'Grams of Fat: {gramsFat:,}')
    print(f'Result calories: {caloriesFat:,}')
    print(f'Grams of Carbs: {gramsCarbs:,}')
    print(f'Result calories: {caloriesCarbs:,}')

# Call main function to start program
main()
