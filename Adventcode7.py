liste_couleurs =[]
liste_bags = []

class color:
    
    def __init__(self, str1,str2):
        """
        str1 always the adjective,
        str2 always the noun
        """
        self.adj = str1
        self.couleur = str2

def color_create(string):
    """
    create a function to create a color
    """
    temp_list = string.split()

    new_color = color(temp_list[0].strip(),temp_list[1].strip())

    if new_color not in liste_couleurs:
        liste_couleurs.append(new_color)
    return new_color

def color_sep(string1):

    if string1.find('no other bags') != -1:
        print("no other bags")
        return 0

    inforamtion_list = []

    temp_color = string1.split(', ')

    for couleur in temp_color:

        temp_elem = couleur.split()

        for word in range(0,len(temp_elem)-1):
        
            temp_elem[word].strip()

            if temp_elem[word].isdecimal():
                inforamtion_list.append(temp_elem[word])
                temp_elem.pop(word)
                word -= 1

            elif temp_elem[word].find('bag') != -1:
                temp_elem.pop(word)
                word -= 1
            
        inforamtion_list.append( color_create(' '.join(temp_elem)) )
        print( color_create(' '.join(temp_elem)).adj )
    return inforamtion_list
        


class bags(color):
    #my_bag = "color"
    
    def __init__(self, string):
        """
        dans le bur de crée toutes les couleurs
        """
        separateur1 = string.find("bags")

        color_bag = string[0:separateur1].strip()
        contain_bags = string[separateur1+12:]

        self.my_bag = color_create(color_bag)

        self.can_bag = color_sep(contain_bags)

with open('colourstest.txt','r') as fh:
    for line in fh:
        liste_bags.append(bags(line))

for i in liste_bags:
    #print("bag of ",i.my_bag.adj,' ', i.my_bag.couleur)
    for j in i.can_bag:
        #print("containing: ", j.couleur,' ', j)
        pass

        