#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    temp=[0 for _ in range(n+2)]
    # O(m x n) time complexity
    '''
    size=len(queries)
    for i in range(size):
        a=queries[i][0]
        b=queries[i][1]
        k=queries[i][2]
        for j in range(a,b+1):
            temp[j]=temp[j] + k
    '''
    # O(m+n) time complexity
    for i in range(len(queries)):
        a=int(queries[i][0])
        b=int(queries[i][1])
        k=int(queries[i][2])
        temp[a] +=k
        if b<=len(temp)-1:
            temp[b+1]=temp[b+1]-k
    
    maximum=0
    sub_total=0
    for j in range(1,len(temp)):
        #temp[j]=temp[j]+temp[j-1] , this can work but it takes much time compare with the under stated statements specially for large number of array/list 
        sub_total +=temp[j]
        if maximum <sub_total:
            maximum=sub_total
      
    return maximum

if __name__ == '__main__':
    file_path=os.getcwd()
    print(file_path)
    file='\OutPut_path.txt'
    try:
        
        fptr = open(file_path+file, 'w')

        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        queries = []

        for _ in range(m):
            queries.append(list(map(int, input().rstrip().split())))

        result = arrayManipulation(n, queries)
        print(result)

        fptr.write(str(result) + '\n')

        fptr.close()
    except OSError:
        print("It is operating systme error  please check permission ",OSError)
        raise
