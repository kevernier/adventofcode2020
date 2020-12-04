WOclass passports():
    byr = "Birth"
    iyr = "Issue"
    eyr = "Expiration"
    hgt = "Height"
    hcl = "Hair"
    ecl = "Eye"
    pid = "Passport"
    cid = "Country"
    
    def __init__(self,byr,iyr,eyr,hgt,hcl,ecl,pid,cid):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid     

def make_passports ( byr,iyr,eyr,hgt,hcl,ecl,pid,cid ):
    person = passports(byr,iyr,eyr,hgt,hcl,ecl,pid,cid)
    return person

temps = []

passports = []

with open('passports.txt', 'r') as fh:
    for line in fh:
        temps.append(line.strip())

my_string =""        
for line in temps:
    if len(line)>1:
        my_string += line
    else:
        passports.append(my_string)
        my_string=""
    


for post in passports:
    print(post)
print(passports)       