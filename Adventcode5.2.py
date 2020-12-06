rows=[]
column=[]
seat_id =[]

def midpoint(point):
    return int(round((point[0] + point[1])/2))

with open('boarding.txt', 'r') as fh:
    for line in fh:
        start =[0,127]
        startc=[0,7]
        for l in line[:6]:
            if l == "F":
                start[1] =  midpoint(start)-1
            else:
                start[0]= midpoint(start)
        if line[6]=="F":
            rows.append(start[0])
        else:
            rows.append(start[1])
        
        for l in line [7:9]:
            if l == "L":
                startc[1] =  midpoint(startc)-1
            else:
                startc[0]= midpoint(startc)
        if line[9]=="L":
            column.append(startc[0])
        else:
            column.append(startc[1])
        seat_id.append((rows[-1]*8) + column[-1])

        
seat_id.sort()
for i in range(1,len(seat_id)-1):
    if seat_id[i]-seat_id[i-1] > 1:
        print("my id = ", seat_id[i]-1)
