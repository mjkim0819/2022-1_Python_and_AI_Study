import math
import os
import random
import re
import sys
 
def insertionSort1(n, arr):
    i = n-1
    last = arr[-1]
  
    while i > 0 and arr[i-1] > last:
        
        arr[i] = arr[i-1]
        print(*arr)
        i = i- 1
    arr[i] = last
    print(*arr)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
