import string
string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
import random

S = []
rule = []
x = 0
di = []
Z = S




def sequitur():
    global s
    s = "ababa"


    for char in s:
        if len(S) < 4:
            S.append(char)
        else:

            check_digram()
            S.append(char)


def check_digram():
    #print(len(S))
    global x
    y = 1
    for i in range( x,len(S)-1):
        print("i:",i)
        print("prima",di)
        print("len(S)-1: ",len(S)-1)
        if i < len(S)-1:

            di.append(S[i]+S[i+1])

            print("dopo",di)
        if di.count(S[i]+S[i+1]) >= 2:
            name_rule = random.choice(string.ascii_uppercase)
            print("di.count(S[i]+S[i+1]):",di.count(S[i]+S[i+1]))
            while name_rule in rule:
                name_rule = random.choice(string.ascii_uppercase)

            if len(rule) == 0:
                print("lunghezza rule: ",len(rule))
                rule.append((name_rule,S[i]+S[i+1]))
                rule_dict=dict((y,x) for x,y in rule)
                print(rule_dict)

                for _ in range(0, len(Z)-1):

                    if y < len(Z)-2:
                        digramma = Z[y-1]+Z[y]

                        if digramma in rule_dict:
                            Z[y-1] = rule_dict[Z[y-1]+Z[y]]
                            print("char:",Z[y-1])
                            Z.remove(Z[y])

                    y = y + 1
                y = 0
                print("nuova Z:",Z)


            for _ in di:
                if _ == S[i]+S[i+1]:
                    di.remove(_)

            else:
                print("wwwwwwwwwww")
                if S[i]+S[i+1] not in (item[1] for item in rule):
                    rule.append((name_rule,S[i]+S[i+1]))
        print("rule: ",rule)
        x =x+2







sequitur()
