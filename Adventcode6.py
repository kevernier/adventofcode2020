documents = []
groups = []
group = ""

with open ('customs.txt','r') as fh:
for line in fh:
  documents.append(line)

for line in documents:
  if line != "\n":
    group += line
  else: #it is a newgroup
    groups.append(group)
    groups = ""

total = 0
for c in groups:
  newset = set(c)
  c = list(newset)
  total += len(c)
