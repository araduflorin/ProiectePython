CNP = {'S': [], 'AA': 0, 'LL': 0, 'ZZ': 0, 'JJ': 0, 'NNN': 0, 'C': 0}
S = ['1','2','3','4','5','6','7','8','9']
AA = []
# print(S)


def validare_S(nr_S):
    list(nr_S)
    # nr_S[0] = int(input(""))
    while nr_S[0] not in S:
        nr_S = input("Prima cifra trebuie sa fie intre 1 si 9: ")
    return nr_S

def validare_AA(nr_An):
    list(nr_An)
    while nr_An[1-3] >= str(23):
        nr_An = input("Cifrele 2 si 3 tr sa fie < 24: ")
    return nr_An

def validare_input_numar(nr):
    validare_S(nr)
    validare_AA(nr)
    # l = list(nr[0])
    for i in range(len(nr)):
        # print(list(nr[0]))
        if str(nr).isdigit() is False:
            nr = input("Introdu doar cifre: ")
        elif len(nr) != 13:
            nr = input("Introdu 13 cifre: ")

        # elif l == 0:
        #     print(list(nr[0]))
        #     nr = input("Introdu o cifra intre 1 si 9: ")

        # l = list(nr)
        # print(nr_S)
        # elif l[0] = 0:
        #
    return nr

def input_CNP():
    return validare_input_numar(input("Introdu CNP-ul format din 13 cifre: "))

c=input_CNP()
print(c)


# Valideaza S
