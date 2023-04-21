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