#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/bin/python3

import math
import os
import random
import re
import sys

def rotate(a,d):
    temp=[]
    for i in range(d):
        temp.insert(len(temp),a.pop(0))
    return a+temp


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    rotated_a=rotate(a,d)
    for i in range(len(rotated_a)):
        print(rotated_a[i],end=" ")


# In[ ]:




