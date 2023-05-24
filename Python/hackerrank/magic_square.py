"""
We define a magic square to be an n * n matrix of distinct positive integers from 1 to n^2
where the sum of any row, column, or diagonal of length n is always equal to the same number: the magic constant.
You will be given a 3 * 3 matrix 's' of integers in the inclusive range [1,9].
We can convert any digit a to any other digit b in the range [1,9] at cost of |a-b|.
Given 's', convert it into a magic square at minimal cost. Print this cost on a new line.

Example

$s = [[9, 3, 4], [1, 5, 8], [6, 4, 2]]

The matrix looks like this:
9 3 4
1 5 8
6 4 2

We can convert it to the following magic square:

8 3 4
1 5 9
6 7 2

This took three replacements at a cost of |5-8| + |8-9| + |4-7| = 7.
"""

def formingMagicSquare(s):
    # Write your code here
    possible_magic_squares = [
        [6, 1, 8, 7, 5, 3, 2, 9, 4], #0
        [8, 1, 6, 3, 5, 7, 4, 9, 2], #1
        [6, 7, 2, 1, 5, 9, 8, 3, 4], #2
        [8, 3, 4, 1, 5, 9, 6, 7, 2], #3
        [2, 7, 6, 9, 5, 1, 4, 3, 8], #4
        [4, 3, 8, 9, 5, 1, 2, 7, 6], #5
        [2, 9, 4, 7, 5, 3, 6, 1, 8], #6
        [4, 9, 2, 3, 5, 7, 8, 1, 6], #7
    ]

    s = [x for y in s for x in y]  # Flattening the input to compare

    costs = list()

    for i in possible_magic_squares:
        cost = sum( [ abs(x[0] - x[1] ) for x in zip(i, s)  ]  )
        costs.append((cost))

    return min(sorted(costs, reverse= False))


s = [[9, 3, 4], [1, 5, 8], [6, 4, 2]]
result = formingMagicSquare(s)
