

def init():
    return input("Inserire il codice separado da uno spazio \n").lower().split(",")


def run():
    table.append(s0)

    createS1(table[0])


def createS1(table1):
    tmp = list()
    for elm1 in table1:
        for elm2 in table1:
            if elm1 != elm2:
                if elm1.find(elm2) == 0:
                    tmp.append(elm1[len(elm2):])

    table.append(list(set(tmp)))
    print(table[0])

if __name__ == '__main__':
    s0 = list(init())
    table = list()
    run()
    # abc abcd e dba bace ceac ceab eadb
    # 0 10 110 1110
