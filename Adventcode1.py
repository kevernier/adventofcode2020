
from math import *

num_list = []

with open('advent.txt', 'r') as fh:
    for line in fh:
        num_list.append(int(line))

total=0

#print(num_list)

for a in num_list:
    for x in num_list:
        for b in num_list:
            total = a + x + b
            if total == 2020:
                print(a)
                print(b)
                print(x)
                print( a*x*b)
                break
            if total == 2020:
                break
        if total == 2020:
            break
    if total == 2020:
        break
