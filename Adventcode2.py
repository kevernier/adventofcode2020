from math import *


results = 0

''' PART 1
with open('passwords.txt', 'r') as fh:
    for line in fh:
        x = line.split()
    	
        temp = x[0].split("-")
        minus=int(temp[0])
        maximus=int(temp[1])

        search_list = x[1][:-1]
        x[2].strip("\n")
        if x[2].count(search_list) >= minus and x[2].count(search_list) <=maximus :
            results +=1
'''

'''PART 2 '''
with open('passwords.txt', 'r') as fh:
    for line in fh:
        x = line.split()
        temp = x[0].split("-")
        minus=int(temp[0])
        maximus=int(temp[1])
        minus = minus-1
        maximus = maximus-1

        search_list = x[1][:-1]
        x[2].strip("\n")
        if bool(x[2][minus]==search_list) ^ bool(x[2][maximus]==search_list):
            results +=1
        #print(minus, maximus)

print(results)