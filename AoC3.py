f = open("input4.txt","r")





#if len(l) == 1: new passport
fields = {
    "byr":False,
    "iyr":False,
    "eyr":False,
    "hgt":False,
    "hcl":False,
    "ecl":False,
    "pid":False
}

count = 0
flds = fields.copy()
for l in f.readlines():
    if len(l) == 1:
        valid = True
        for k in flds.keys():
            if not flds[k]:
                valid = False
        if valid:
            count += 1
        flds = fields.copy()
    else:
        line = l[:-1]
        line = line.split(" ")
        for w in line:
            word = w.split(":")[0]
            value = w.split(":")[1]
            for k in flds.keys():
                if word == k:
                    flds[k] = True
                    if word == "byr":
                        if not (int(value) >= 1920 and int(value) <= 2002):
                            flds[k] = False
                    elif word == "iyr":
                        if not (int(value) >= 2010 and int(value) <= 2020):
                            flds[k] = False
                    elif word == "eyr":
                        if not (int(value) >= 2020 and int(value) <= 2030):
                            flds[k] = False
                    elif word == "hgt":
                        if value[-2:] == "cm":
                            if not (int(value[:-2]) >= 150 and int(value[:-2]) <= 193):
                                flds[k] = False
                        elif value[-2:] == "in":
                            if not (int(value[:-2]) >= 59 and int(value[:-2]) <= 76):
                                flds[k] = False
                        else:
                            flds[k] = False
                    elif word == "hcl":
                        val = True
                        if value[0] == "#" and len(value) == 7:
                            valids = ["0","1","2","3","4","5","6","7","8","9",'a','b','c','d','e','f']

                            for i in range(1,7):
                                if value[i] not in valids:
                                    val = False
                            if not val:
                                flds[k]= False
                        else:
                            flds[k] = False
                    elif word == "ecl":
                        valids = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                        if value not in valids:
                            flds[k] = False
                    elif word == "pid":
                        if not (len(value)==9 and int(value) >= 0):
                            flds[k] = False


valid = True
for k in flds.keys():
    if not flds[k]:
        valid = False
if valid:
    count += 1
flds = fields.copy()

print(count)
