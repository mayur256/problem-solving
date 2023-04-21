"""
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an uphill, , or a downhill,  step. Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

Example 
steps=8 path=[DDUUUUDD]
The hiker first enters a valley  units deep. Then they climb out and up onto a mountain  units high. Finally, the hiker returns to sea level and ends the hike.
"""
# func definition
def countingValleys(steps, path):
    # Write your code here
    valley_count = 0
    current_hike_level = 0 # Starting with sea-level
    in_valley = False

    for hillType in path:
        if hillType == 'U': #uphill
            current_hike_level = current_hike_level + 1
        else:
            current_hike_level = current_hike_level - 1

        if not in_valley and current_hike_level < 0:
            in_valley = True
            valley_count = valley_count + 1
        elif current_hike_level == 0:
            in_valley = False
    
    return valley_count

# Test cases
print(countingValleys(4, ['D', 'D', 'U', 'U']))