"""
Test effettuati a partire dai seguenti codici:
- a,c,ad,abb,bad,deb,bbcde => Il codice non è UD a causa dell'intersezione non vuota tra l'insieme S0 e l'insieme S5
- abc,abcd,e,dba,bace,ceac,ceab,eabd => Il codice è UD poichè l'insieme S4 è uguale all'insieme S7
- 010,0001,0110,1100,00011,00110,11110,101011 => Il codice non è UD a causa dell'intersezione non vuota tra l'insieme S0 e l'insieme S6
- 00,01,10,11 => Codice UD poichè l'insieme S1 è vuoto
- 0,10,110,1110 => Codice UD poichè l'insieme S1 è vuoto
"""


def init():
    return input("Inserisci elementi codice separati dal carattere , \n").lower().split(",")


def compute():
     collection.append(codeElement)
     createFirstCollection(collection[0])

     i = 2
     while checkCondition() == 1:
         createCollection(collection[0], collection[i-1])
         i = i + 1
     printCollections()


#funzione per verificare le condizioni di arresto
def checkCondition():
    set0 = set(collection[0])
    for i in range(1, len(collection)):
        seti = set(collection[i])
        #condizione 1, se esiste i>0 tale che intersezione tra S0 ed Si != 0 => codice non è UD
        if len(set0.intersection(seti)) != 0:
            print("Il codice non è UD a causa dell'intersezione non vuota tra l'insieme S0 e l'insieme S{}".format(i))
            return 0
        #condizione 2, se esiste i>0, tale che Si = 0 => codice UD
        if len(seti) == 0:
            print("Codice UD poichè l'insieme S{} è vuoto".format(i))
            return 0
        #condizione3, se esistono i,j > 0, Si = Sj => codice è UD
        for j in range(i+1, len(collection)):
            setj = set(collection[j])
            if (seti.issubset(setj)) or (setj.issubset(seti)):
                print("Il codice è UD poichè l'insieme S{} è uguale all'insieme S{}".format(i, j))
                return 0
    return 1


#Funzione apposita per creare S1, considerando che solo per questo caso specifico all'interno dei due cicli for
#avremo il confronti tra due elementi uguali
def createFirstCollection(collection1):
    tmp = list()
    for element1 in collection1:
        for element2 in collection1:
            if element1 != element2:
                if element1.find(element2) == 0:
                    tmp.append(element1[len(element2):])
                else:
                    if element2.find(element1) == 0:
                        tmp.append(element2[len(element1):])
    collection.append(list(set(tmp)))

#semplicemente creo due cicli for per il confronto tra l'insieme S0 e l'insieme Si
def createCollection(collection1, collection2):
    tmp = list()
    for elementCollection1 in collection1:
        for elementCollection2 in collection2:
            if elementCollection1.find(elementCollection2) == 0:
                #una volta che un elemento è prefisso di un altro, semplicemente copio tutta la stringa a partire dal prefisso
                # (escluso)
                tmp.append(elementCollection1[len(elementCollection2):])
            else:
                if elementCollection2.find(elementCollection1) == 0:
                    tmp.append(elementCollection2[len(elementCollection1):])
    collection.append(list(set(tmp)))


def printCollections():
    i = 0
    for coll in collection:
        print("S{}".format(i))
        for element in coll:
            print(element)
        i = i+1


if __name__ == '__main__':
    #elementi del codice, che identifica il nostro S0
    codeElement = list(init())
    #lista di liste, dove ogni lista compone i vari Si
    collection = list()
    compute()

#prova prova