import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    # Write your code here
    charecter = ''
    result = 0
    for i in s:
        if i != charecter:
            charecter = str(i)
        elif i == charecter:
            result += 1
    return result
            
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)
        print(result)
    #     fptr.write(str(result) + '\n')

    # fptr.close()