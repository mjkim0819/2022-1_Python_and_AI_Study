import math
import os
import random
import re
import sys


def countingSort(arr):
    arr1 = [0]*100
    for i in range(0,n):
        A = arr[i]
        arr1[A] += 1
    arr2=[]
    for i in range(100):
        while arr1[i]>0:
            arr2.append(i)
            arr1[i]-=1
    return arr2
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
