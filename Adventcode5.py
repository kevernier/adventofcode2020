rows=[]
column=[]
seat_id =[]
id_max=0

def midpoint(point):
    #print(int(round((point[0] + point[1])/2)))
    return int(round((point[0] + point[1])/2))

with open('boarding.txt', 'r') as fh:
    for line in fh:
        start =[0,127]
        startc=[0,7]
        #print(line[9],line[7])
        #print("newline")
        for l in line[:6]:
            #print("mid",midpoint(start))
            if l == "F":
                start[1] =  midpoint(start)-1
            else:
                start[0]= midpoint(start)
            #print("start",start)
        if line[6]=="F":
            rows.append(start[0])
        else:
            rows.append(start[1])
        
        for l in line [7:9]:
            if l == "L":
                startc[1] =  midpoint(startc)-1
            else:
                startc[0]= midpoint(startc)
            #print(startc)
        if line[9]=="L":
            column.append(startc[0])
        else:
            column.append(startc[1])
        start.clear()
        startc.clear()
        seat_id.append((rows[-1]*8) + column[-1])
        if seat_id[-1]>id_max:
            id_max=seat_id[-1]
        

for i,k in zip(rows,column):
    print(i,k," id ", i*8 + k)
    seat_id.append(i*8 + k)
print(id_max)
print("max with max(): ",max(seat_id))
