#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

digDict = {'10': 1,
           '11': 2,
           '12': 3,
           '13': 4}


def find_super_digit(n):
    if len(n) == 1:
        return n

    v = digDict.get(n)

    if v is not None:
        return find_super_digit(str(v))

    sum = 0
    for d in n:
        sum = sum + int(d)

    digDict[n] = sum

    return find_super_digit(str(sum))


def superDigit(n, k):
    # Write your code here
    if len(n) == 1:
        return n

    v = find_super_digit(n)

    v = int(v)*k

    return find_super_digit(str(v))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()