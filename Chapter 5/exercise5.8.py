# Global constants
LABOR_CHARGE = 35
LABOR_HOURS = 8
FEET_PER_GALLON = 112

# Define main function
def main():
    feetWall = getSpace()
    pricePaint = getPrice()
    gallonPaint = setPaint(feetWall)
    hourLabor = setHours(gallonPaint)
    costLabor = setLaborCharge(hourLabor)
    costPaint = setPaintCharge(gallonPaint, pricePaint)
    showIncome(gallonPaint, hourLabor, costPaint, costLabor)

# Define function to get wall space
def getSpace():
    feetWall = int(input('Enter square footage of wall space: '))
    return feetWall

# Define function to get price of the paint
def getPrice():
    pricePaint = int(input('Enter price of paint per gallon: '))
    return pricePaint

# Define function to calculate the gallons of paint needed
def setPaint(feetWall):
    gallonPaint = feetWall / FEET_PER_GALLON
    return gallonPaint

# Define function to calculate the hours of labor required
def setHours(gallonPaint):
    hourLabor = gallonPaint * LABOR_HOURS
    return hourLabor

# Define function to calculate the cost of labor
def setLaborCharge(hourLabor):
    costLabor = hourLabor * LABOR_CHARGE
    return costLabor

# Define function to calculate the cost of paint
def setPaintCharge(gallonPaint, pricePaint):
    costPaint = gallonPaint * pricePaint
    return costPaint

# Define function to display invoice
def showIncome(gallonPaint, hourLabor, costPaint, costLabor):
    totalCost = costPaint + costLabor
    print(f'Gallons of paint: {gallonPaint:,.2f}')
    print(f'Hours of labor: {hourLabor:,.2f}')
    print(f'Paint charges: ${costPaint:,.2f}')
    print(f'Labor charges: ${costLabor:,.2f}')
    print(f'Total cost: ${totalCost:,.2f}')

# Call main function to start program
main()
    
