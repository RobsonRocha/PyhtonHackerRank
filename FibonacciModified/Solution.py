#!/bin/python3

import math
import os
import random
import re
import sys


def fibo(n, cache):
    try:
        return cache[n]
    except:
        pass

    powered = fibo(n - 1, cache)
    calc = fibo(n - 2, cache) + powered * powered
    cache.append(calc)
    return calc


# Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
    cache = [t1, t2]

    return fibo(n - 1, cache)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()

