tab = [(1,1),(3,1),(5,1),(7,1),(1,2)]
forest = []
res = 1

with open('day3.txt', 'r') as fh:
    for line in fh:
        forest.append(line.strip('\n'))

for (tab_x, tab_y) in  tab:
    x = 0
    y = 0
    tree = 0
    while y < len(forest) and x < len(forest[0]):
        if forest[y][x]=="#":
            tree+=1
            x+= tab_x
            y+= tab_y
            x -= len(forest[0])
print(res)