documents = []
group = []
my_string = ""

def removeDuplicate(str): 
    index = 0
    for i in range(0, len(str)): # Traverse through all characters 
        for j in range(0, i + 1): # Check if str[i] is present before it  
            if (str[i] == str[j]): 
                break

        if (j == i): 
            str[index] = str[i] 
            index += 1
              
    return "".join(str[:index]) 

with open ('customs.txt','r') as fh:
  for line in fh:
    documents.append(removeDuplicate(list(line)))

for i in range(0,len(documents)):
  if documents[i] !='\n':
    my_string += documents[i].strip('\n')
    if i==(len(documents)-1):
      group.append( removeDuplicate(list(my_string ) ) )
  else:
    group.append(removeDuplicate(list(my_string)))
    my_string=""

total = 0
for answer in group:
  total += len(answer)
print(total)