import string
string.ascii_uppercase
import random

def split(word):
    return [char for char in word]

x = 0
def sequitur(s):
    global x
    list_s = split(s[0:4])
    digram = []
    rule = {}
    for i in range(3,len(s)):
        if len(digram) == 0:
            for i in range(0,len(list_s)-1):
                digram.append(list_s[i]+list_s[i+1])
            if digram.count(list_s[i]+list_s[i+1]) >= 2:
                name_rule = random.choice(string.ascii_uppercase)
                while name_rule in rule:
                    name_rule = random.choice(string.ascii_uppercase)
                rule[list_s[i]+list_s[i+1]] = name_rule
                x = 2
                print("primi digram:",digram)

                for i in range(0,len(list_s)-2):
                    #print(len(list_s))
                    if  list_s[i]+list_s[i+1] in rule:
                        #print(list_s[i]+list_s[i+1])
                        #print(list_s)
                        list_s[i] = rule[list_s[i]+list_s[i+1]]
                        list_s.remove(list_s[i+1])
                        #print(list_s)




        else:

            digram = []
            print("prima lista",list_s)
            list_s.append(s[len(list_s)+x])
            print("dopo lista",list_s)
            for i in range(0,len(list_s)-1):
                digram.append(list_s[i]+list_s[i+1])

            if digram.count(list_s[i]+list_s[i+1]) >= 2:
                name_rule = random.choice(string.ascii_uppercase)
                while name_rule in rule:
                    name_rule = random.choice(string.ascii_uppercase)
                rule[list_s[i]+list_s[i+1]] = name_rule
                x = 2
                print("digrammi dopo",digram)


            for i in range(0,len(list_s)-2):
                #print(len(list_s))
                if  list_s[i]+list_s[i+1] in rule:
                    #print(list_s[i]+list_s[i+1])
                    #print(list_s)
                    list_s[i] = rule[list_s[i]+list_s[i+1]]
                    list_s.remove(list_s[i+1])
                    #print(list_s)




            print(list_s)





sequitur("abcdbcabcd")
