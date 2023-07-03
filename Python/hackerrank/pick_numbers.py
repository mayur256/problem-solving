"""
Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.

Example
a=[1,1,2,2,4,4,5,5,5]

There are two subarrays meeting the criterion: [1,1,2,2] and [4,4,5,5,5]. The maximum length subarray has 5 elements.
"""

#Solution
def pickingNumbers(a):
    # Write your code here
    a.sort()
    print(a)
    maxSubArrLen = 0
    for i in range(len(a)):
        subArr=[]
        subArr.append(a[i])
        for j in range(i+1,len(a)):
            if abs(a[i]-a[j])==0 or abs(a[i]-a[j])==1:
                subArr.append(a[j])
        maxSubArrLen=max(len(subArr), maxSubArrLen)
        
    return maxSubArrLen
    
result = pickingNumbers([1, 2, 2, 3, 1, 2])
print(result)