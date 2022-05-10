# Global Constants
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

# Define main funtion
def main():
    purchase = getPurchase()
    stateTax = setStateTax(purchase)
    countyTax = setCountyTax(purchase)
    showSale(purchase, stateTax, countyTax)

# Function that gets the purchase amount from the user
def getPurchase():
    purchaseAmount = float(input('Enter amount of purchase: '))
    return purchaseAmount

# Function that calculates state sales tax
def setStateTax(purchase):
    stateTax = purchase * STATE_TAX_RATE
    return stateTax

# Function that calculates county sales tax
def setCountyTax(purchase):
    countyTax = purchase * COUNTY_TAX_RATE
    return countyTax

# Function that displays the sale information
def showSale(purchase, stateTax, countyTax):
    # Calculate the total amount of sales tax
    totalTax = stateTax + countyTax
    # Calculate the total amount of the sale
    totalSale = purchase + totalTax
    # Display all sales info
    print(f'Purchase Amount: ${purchase:,.2f}')
    print(f'State sales tax: ${stateTax:,.2f}')
    print(f'County sales tax: ${countyTax:,.2f}')
    print(f'Total sales tax: ${totalTax:,.2f}')
    print(f'Total of sale: ${totalSale:,.2f}')

# Call the main funtion to start the program
main()
