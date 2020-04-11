
def bwt_coding(start):
    w = [start]
    w = rotate_sort(w)

    L = find_L(w)
    L_str = ''.join(L)

    F = find_F(w)
    index = find_I(w, start)

    print("\nINPUT: {}".format(start))
    print("Lista ordinata: {}".format(w))
    print("BWT({})= {}, {}".format(start, L_str, index))
    return F, L, index


def rotate_sort(a):
    j = 0
    while j < len(a[0]) - 1:
        a.append(a[j][1:len(a[j])] + a[j][0])
        j += 1
    a.sort()
    return a


def find_L(a):
    l = list()
    for i in a:
        l.append(i[len(a) - 1])
    return l


def find_F(a):
    f = list()
    for i in a:
        f.append(i[0])
    return f


def find_I(a, input):
    j = 0
    for i in a:
        if i == input:
            return j
        j += 1


def create_t():
    tau = list()
    for i in f:
        x = 0
        for j in temp_l:
            if i == j:
                tau.append(x)
                temp_l[x] = ""
            x += 1
    return tau


def bwt_decoding():
    output = list()
    I = i
    for j in range(0, len(l)):
        if j == 0:
            output.insert(0, f[I])
        else:
            output.insert(j, f[t[I]])
            I = t[I]

    output = ''.join(output)
    return output


if __name__ == '__main__':
    f, l, i = bwt_coding("abraca")
    temp_l = l.copy()
    t = create_t()
    o = bwt_decoding()
    print("F : {}".format(f))
    print("L : {}".format(l))
    print("T : {} ".format(t))
    print("OUTPUT : {} ".format(o))
