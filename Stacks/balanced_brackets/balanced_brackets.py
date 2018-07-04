#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    for _ in s:
        stack.append(_)
    i = -1
    while(stack):
        if abs(i)>=len(stack):
            break
        t = stack[i]
        if (t == '}' and stack[i-1] == '{') or (t == ']' and stack[i-1] == '[') or (t == ')' and stack[i-1] == '(') :
            stack.pop(i)
            stack.pop(i)
            i = i+1
        else:
            if abs(i-1)<=len(stack):
                i = i-1
            else:
                break

    if stack:
        return 'NO'
    else:
        return 'YES'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
