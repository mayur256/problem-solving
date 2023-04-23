"""
A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget.
Given price lists for keyboards and USB drives and a budget, find the cost to buy them.
If it is not possible to buy both items, return -1.
For e.g
budget = 60
keyboards = [40,50,60]
drives = [5,8,12]

The person can buy a 40 keyboard + 12 drive = 52, or a 50 keyboard + 8 USB drive = 58. Choose the latter as the more expensive option and return 58.
"""

# Solution definition
def getMoneySpent(keyboards, drives, maxBudget):
    # Code goes here
    totalPurchase = []
    maxVal = 0

    for keybaord in keyboards:
        for drive in drives:
            total = keybaord + drive

            if total <= maxBudget:
                totalPurchase.append(total)
    
    if len(totalPurchase) > 0:
        maxVal = max(totalPurchase)

    return maxVal if maxVal > 0 else -1

# Test cases
print(getMoneySpent([10, 2, 3], [5,2,8], 31))