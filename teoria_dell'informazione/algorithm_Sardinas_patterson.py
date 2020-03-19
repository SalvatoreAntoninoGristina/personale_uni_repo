"""
Salvatore Antonino Gristina
abc abcd e dba bace ceac ceab eabd
a c ad abb bad deb bbcde
00 01 10 11
0 10 110 1110
a c ad abb bad deb bbcde
"""


def init():
    return input("Inserire il codice separado ogni elemento da uno spazio \n").split(" ")


def run():

    table.append(s0)    # inserisco la colonna all'interno della tabella

    i = create_and_check_S1(table[0])    # creo S1

    while i != 0:
        # creo colonne finchè non arrivo ad una condizione di arresto
        i = create_and_check_Sn(table[0], table[i], i)

    print_table()


def create_and_check_S1(table1):
    tmp = list()
    for elem1 in table1:
        for elem2 in table1:
            if elem1 != elem2:
                if elem1.find(elem2) == 0:    # controllo se una parola è prefisso dell'altra
                    tmp.append(elem1[len(elem2):])

    if len(tmp) == 0:    # primo caso di arresto
        print("Il codice è UD poiché S1 è vuoto")
        return 0
    else:
        table.append(list(set(tmp)))    # aggiungo s1

    return 1


def create_and_check_Sn(S0, Si, i):
    tmp = list()
    for elem1 in S0:
        for elem2 in Si:
            if elem1 != elem2:
                if elem1.find(elem2) == 0:
                    tmp.append(elem1[len(elem2):])
                else:
                    if elem2.find(elem1) == 0:
                        tmp.append(elem2[len(elem1):])
    if len(tmp) == 0:
        print("Il codice è UD poiché S{} è vuoto." .format(i + 1))
        return 0
    else:
        table.append(list(set(tmp)))

        set0 = set(table[0])
        seti = set(table[i + 1])

        for j in range(len(table) - 1):
            setj = set(table[j])
            if setj == seti:    # secondo caso di arresto
                print(
                    "Il codice è UD poichè l'insieme S{} è uguale all'insieme S{}".format(i + 1, j))

                return 0

        if len(set0.intersection(seti)) != 0:    # terzo caso di arresto
            print(
                "Il codice non è UD perchè l'insieme S0 e l'insieme S{} hanno elementi in comune".format(i + 1))
            return 0

    return i + 1


def print_table():

    for i in range(0, len(table)):
        print("S{}: {} ".format(i, table[i]))


# main dove creo una tabella e la prima colonna S0
if __name__ == '__main__':
    s0 = list(init())
    table = list()
    run()
