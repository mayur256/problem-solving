bill = [3,10,2,9]
k = 1
b = 12

def bonAppetit(bill, k, b):
    grossBill = sum(bill) // 2
    annieBill = sum([bill[i] for i in range(len(bill)) if i != k]) // 2
    diff = b - annieBill
    return diff if diff > 0 else 'Bon Appetit' 
    
print(bonAppetit(bill, k, b))
