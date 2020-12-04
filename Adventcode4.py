import string

id_format_p =[
    "0123456789",
    "0123456789",
    "0123456789",
    "0123456789",
    "0123456789",
    "0123456789",
    "0123456789",
    "0123456789",
    "0123456789",
]
id_format_e=[
    "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
]

class papier(object):
    byr = "Birth"
    iyr = "Issue"
    eyr = "Expiration"
    hgt = "Height"
    hcl = "Hair"
    ecl = "Eye"
    pid = "Passport"
    cid = "Country"

    def validate_hair(self):
        if len(self.hgt)==7:
            if self.hgt[0]=="#":
                return True
        return False

    def validate_height(self):
        if len(self.hgt)>=4:
            if self.hgt[-2:] == "in":
                if 59<= int(self.hgt[:-2]) <=76:
                    return True
            else:
                if 150<= int(self.hgt[:-2]) <=193:
                    #print(self.hgt[:-2])
                    return True
        return False

    def validate(self):
        if self.byr == "Birth" or not(  1920 <= self.byr <= 2002) :
            #print("birth")
            return False
        if self.iyr == "Issue" or not( 2010 <= self.iyr <= 2020):
            #print("Issue")
            return False
        if self.eyr == "Expiration" or not( 2020 <= self.eyr <= 2030):
            #print("Expiration")
            return False
        if self.hgt == "Height" or not self.validate_height():
            #print("HGT")
            return False
        if self.hcl == "Hair" :#or not self.validate_hair():
            #print("Hair")
            return False
        if self.ecl == "Eye" or ( all(c in id_format_e for c in self.ecl)):
            #print("Eye")
            return False
        if self.pid == "Passport" or (all(c in id_format_p for c in self.pid)):
            #print("Pays")
            return False
        if self.cid == "Country" or self.cid != "Country":
            #print("country")
            return True
    

    def __init__(self,
    byr = "Birth",
    iyr = "Issue",
    eyr = "Expiration",
    hgt = "Height",
    hcl = "Hair",
    ecl = "Eye",
    pid = "Passport",
    cid = "Country"):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid     

def make_papier ( byr,iyr,eyr,hgt,hcl,ecl,pid,cid ):
    person = papier(byr,iyr,eyr,hgt,hcl,ecl,pid,cid)
    return person

temps = []
passports = []
infos = []

with open('passportstest.txt', 'r') as fh:
    for line in fh:
        temps.append(line.strip())

my_string =""        
for line in temps:
    if len(line)>1:
        my_string += (line+ ' ')
    else:
        passports.append(my_string)
        my_string=""
passports.append(my_string)#lastpass because no \n normally    

for ids in passports:
    idee=[]
    idee = ids.split()
    p1 = papier()
    for pos in idee:        
        if pos[:4] == ("byr:"):
            #print(pos[4:])
            p1.byr = int(pos[4:])
        if pos[:4] == ("iyr:"):
            #print(pos)
            p1.iyr = int(pos[4:])
        if pos[:4] == ("eyr:"):
            p1.eyr = int(pos[4:])
        if pos[:4] == ("hgt:"):
            p1.hgt = pos[4:]
        if pos[:4] == ("hcl:"):
            p1.hcl = pos[4:]
        if pos[:4] == ("ecl:"):
            p1.ecl = pos[4:]
        if pos[:4] == ("pid:"):
            p1.pid = pos[4:]
        if pos[:4] == ("cid:"):
            p1.cid = pos[4:]
    infos.append(p1)    
    idee.clear()

valid_passports=0
for post in infos:
        if post.validate():
            valid_passports +=1
print(valid_passports)

#for post in infos:
    #print(post.byr,post.iyr,post.eyr,post.hgt,post.hcl,post.ecl,post.pid,post.cid)
#print(passports)       