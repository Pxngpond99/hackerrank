import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    asc = [ord(a) for a in s]
    s = [abs(asc[i]-asc[i+1]) for i in range(len(asc)-1)]
    if s == s[::-1]:
        return "Funny"
    return "Not Funny"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)
        print(result)
    #     fptr.write(resul
    # 
    # 
    # 
    # t + '\n')

    # fptr.close()