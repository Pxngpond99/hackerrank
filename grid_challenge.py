import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    new_grid = [sorted(t) for t in grid]
    for x in range(len(new_grid[0])):
        columns = [y[x] for y in new_grid]
        if columns != sorted(columns):
            return 'NO'
    return 'YES'

            
            
                
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)
        print(result)
    #     fptr.write(result + '\n')

    # fptr.close()