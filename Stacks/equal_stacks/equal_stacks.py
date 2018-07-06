#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    h1 = h1[::-1]
    h2 = h2[::-1]
    h3 = h3[::-1]
    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)
    if sum1==sum2==sum3:
        return sum1
    while((sum1!=sum2) or (sum2!=sum3) or (sum1!=sum3)):
        if sum1>sum2 or sum1>sum3:
            t = h1.pop()
            sum1 = sum1 - t
        elif sum2>sum1 or sum2>sum3:
            t = h2.pop()
            sum2 = sum2 - t
        else:
            t = h3.pop()
            sum3 = sum3 - t
    return sum1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
