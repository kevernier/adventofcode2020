tab = [(1,1),(3,1),(5,1),(7,1),(1,2)]
forest = []
res = 1

with open('Trees.txt', 'r') as fh:
    for line in fh:
        forest.append(line.strip('\n'))

for (tab_x, tab_y) in  tab:
    x = 0
    y = 0
    tree = 0
    while y < len(forest) :
        while x < len(forest[0]):
            if forest[y][x]=="#":
                tree+=1
            x+= tab_x
            y+= tab_y
            if y >= len(forest):
                break
        x -= len(forest[0])
    res = res*tree
print(res)