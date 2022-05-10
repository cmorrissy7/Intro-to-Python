# Define main function, whichcalculates and displays the total monthly
# and annual expenses
def main():
    monthlyCost = getLoanCost() + getInsuranceCost() + getGasCost() + getOilCost()
    + getTireCost() + getMaintenanceCost() # Adds all monthly costs
    annualCost = monthlyCost * 12
    print(f'Total monthly expenses: ${monthlyCost:,.2f}')
    print(f'Total annual expenses: ${annualCost:,.2f}')

# Define function to get the loan cost from the user
def getLoanCost():
    loan = float(input('Monthly loan payment: '))
    return loan

# Define function to get the insurance cost
def getInsuranceCost():
    insurance = float(input('Monthly insurance payment: '))
    return insurance

# Define function to get the gas cost
def getGasCost():
    gas = float(input('Monthly gas expenses: '))
    return gas

# Define function to get the oil cost
def getOilCost():
    oil = float(input('Monthly oil expenses: '))
    return oil

# Define function to get the tire cost
def getTireCost():
    tires = float(input('Monthly tire expenses: '))
    return tires

# Define function to get the maintenance cost
def getMaintenanceCost():
    maintenance = float(input('Monthly maintenance expenses: '))
    return maintenance
    
# Call the main function
main()
