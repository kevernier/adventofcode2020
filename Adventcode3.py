pos_x = 0
pos_y = 0
right = 3
downwards = 1

crash = 0

with open('day3.txt', 'r') as fh:
    for line in fh:
        line = line[:-1]
        print(pos_x,pos_y, len(line), line)

        if pos_x < len(line):
            if line[pos_x] == "#" and pos_y % downwards == 0:
                crash += 1
            pos_x += right

        else:
            pos_x = pos_x-len(line)
            print("repetition", crash)
            print(pos_x,pos_y, len(line), line)
            if line[pos_x] == "#" and pos_y % downwards == 0:
                crash += 1
            pos_x += right

        pos_y += 1
print(crash)