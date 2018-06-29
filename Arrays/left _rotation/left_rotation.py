#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    b = a[:]
    for i in range(n):
        b[((n-d)+i)%n] = a[i]
    print(" ".join(map(str,b)))
