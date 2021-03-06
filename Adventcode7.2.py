liste_couleurs = []
liste_bags = []
cont_shiny = 0

numberofbags = 1


class Color:

    def __init__(self, str1, str2):
        """
        str1 always the adjective,
        str2 always the noun
        """
        self.adj = str1
        self.couleur = str2

    def __str__(self):
        return self.adj +' '+  self.couleur

def color_create(string):
    """
    create a function to create a color
    """
    temp_list = string.split()

    new_color = Color(temp_list[0].strip(), temp_list[1].strip())

    #if new_color not in liste_couleurs:
        #liste_couleurs.append(new_color)
    return new_color


def color_sep(string1):
    
    inforamtion_list = []

    if string1.find('no other bags') != -1:
        #print("no other bags")
        return inforamtion_list


    temp_color = string1.split(', ')

    for couleur in temp_color:

        temp_elem = couleur.split()

        for word in range(0, len(temp_elem) - 1):

            temp_elem[word].strip()

            if temp_elem[word].isdecimal():
                ''' remettre si besoin d'utiliser la quantité '''
                #quantity_list.append(int(temp_elem[word]))
                temp_elem.pop(word)
                word -= 1

            elif temp_elem[word].find('bag') != -1:
                temp_elem.pop(word)
                word -= 1
        #quantity_list.append(0)    
        inforamtion_list.append( color_create(' '.join(temp_elem)) )
        #print( color_create(' '.join(temp_elem)).adj, ' ' ,color_create(' '.join(temp_elem)).couleur )
    return inforamtion_list

def numerator (string1):

    quantity_list = []

    if string1.find('no other bags') != -1:
        return quantity_list

    temp_color = string1.split(', ')

    for couleur in temp_color:

        temp_elem = couleur.split()

        for word in range(0, len(temp_elem) - 1):

            temp_elem[word].strip()

            if temp_elem[word].isdecimal():
                quantity_list.append(int(temp_elem[word]))
                temp_elem.pop(word)
                word -= 1

            elif temp_elem[word].find('bag') != -1:
                temp_elem.pop(word)
                word -= 1

    return quantity_list


class Bags(Color):
    #my_bag = "color"
    #can_bag c'est une liste de couleur
    
    def __init__(self, string):
        """
        dans le bur de crée toutes les couleurs
        """
        separateur1 = string.find("bags")

        color_bag = string[0:separateur1].strip()
        contain_bags = string[separateur1 + 12:]

        self.my_bag = color_create(color_bag)

        self.can_bag = color_sep(contain_bags)

        self.containing = numerator(contain_bags)
    
def compteur(color):
    global numberofbags
    for i in liste_bags:
        print(str(i.my_bag),str(color))
        if str(i.my_bag) == str(color):
            print("they're equal", len(i.containing))
            for j in range(0, len(i.containing)) :
                numberofbags = numberofbags + i.containing[j]
                print(i.containing[j],"color")
                compteur(i.can_bag[j])
    

with open('colourstest.txt','r') as fh:
    for line in fh:
        liste_bags.append(Bags(line))

for i in liste_bags:
    # print("bag of ",i.my_bag.adj,' ', i.my_bag.couleur)
    for j in i.containing:
        #print("sac", i.my_bag ,"containing: ", j)
        pass

compteur(color_create("shiny gold"))

#print("longeur de liste_couleurs", len(liste_couleurs))
print("le nombre de sac contenu", numberofbags)
