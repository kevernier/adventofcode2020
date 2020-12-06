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

def occurences (Astr,char):
    res = 0
    for i in range(len(Astr)):
        if Astr[i]==char:
            res +=1
    return res

def onlyDuplicate(Astr):
    sameanswer=""
    for letter in Astr:
        if occurences(Astr,letter)==len(Astr.split()):
            sameanswer += letter
    return sameanswer.strip()

with open ('customs.txt','r') as fh:
    for line in fh:
        documents.append(''.join(sorted(line)))


    for i in range(0,len(documents)):
        if documents[i] !='\n':
            my_string = my_string + ' '+ documents[i].strip('\n')
            if i==(len(documents)-1):

                group.append( removeDuplicate(list(onlyDuplicate(my_string) ) ).strip() )#SAME
        else:

            group.append( removeDuplicate(list(onlyDuplicate(my_string) ) ).strip() )#SAME
            my_string=""

total = 0

for answer in group:
    #print("réponses by all: ",answer,len(answer))
    total += len(answer)
print(total)

#print(group)