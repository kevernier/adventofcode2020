k_liste = []
acc = 0

with open('console.txt', 'r') as fh:
    for line in fh:
        k_liste.append(line)

i = 0

while k_liste[i] != "ext" and i < len(k_liste)-1:
    print(k_liste[i])
    if k_liste[i][:3] == "acc":
        acc += int(k_liste[i][4:])
        k_liste[i] = "ext"
        i += 1
    if k_liste[i][:3] == "jmp":
        a=i
        i += int(k_liste[i][4:])
        k_liste[a] = "ext"
    if k_liste[i][:3] == "nop":
        k_liste[i] = "ext"
        i += 1
    print(i, " with max =", len(k_liste))

print(acc)
