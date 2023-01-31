import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    ori_alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_ro = ''
    encrypts = ''
    for i in ori_alpha:
            alpha_ro += ori_alpha[(ori_alpha.index(i)+k)%26]
    for x in s:
        if x.isupper():
            encrypts += alpha_ro[ori_alpha.index(x.lower())].upper()
        elif x in ori_alpha:
            encrypts += alpha_ro[ori_alpha.index(x)]
        else:
            encrypts += x
    return encrypts
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()