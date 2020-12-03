pos_x = 0
pos_y = 0

crash = 0

with open('Trees.txt', 'r') as fh:
    for line in fh:
        line = line[:-1]
        print(pos_x,pos_y%2, len(line), line)

        if pos_x < len(line):
            if line[pos_x] == "#" and pos_y % 2 == 0:
                crash += 1
            pos_x += 7

        else:
            pos_x = pos_x-len(line)
            print("repetition", crash)
            print(pos_x,pos_y, len(line), line)
            if line[pos_x] == "#" and pos_y % 2 == 0:
                crash += 1
            pos_x += 7

        pos_y += 1
print(crash)