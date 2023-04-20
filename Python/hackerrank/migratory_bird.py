def migratoryBirds(arr):
    # Write your code here
    count = [0] * 6
    for x in arr:
    	count[x]+= 1
    	
    return count.index(max(count))
    
    
arr = [1,1,2,2,3]
print(migratoryBirds(arr))
