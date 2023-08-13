"""
A video player plays a game in which the character competes in a hurdle race.
Hurdles are of varying heights, and the characters have a maximum height they can jump.
There is a magic potion they can take that will increase their maximum jump height by 1 unit for each dose.
How many doses of the potion must the character take to be able to jump all of the hurdles.
If the character can already clear all of the hurdles, return 0.
e.g
height = [1,2,3,3,2]
k = 1
Here, The character can jump 1 unit high initially and must take 3-1=2 doses of potion to be able to jump all of the hurdles.
"""

# Solution definiton
def hurdleRace(jumpCapacity, heights):
    # Write code here
    doses = 0
    maxHeight = max(heights)

    if (maxHeight > jumpCapacity):
        doses = maxHeight - jumpCapacity
    
    return doses

print(hurdleRace(1, [1,2,3,3,2]))
