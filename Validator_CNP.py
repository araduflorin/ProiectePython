CNP = {'S': [], 'AA': 0, 'LL': 0, 'ZZ': 0, 'JJ': 0, 'NNN': 0, 'C': 0}
# S = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
AA = []


# print(S)
def validare_S(nr_S):
    S = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while (nr_S[0]) not in S:
        nr_S = input("Prima cifra trebuie sa fie intre 1 si 9: ")
        while int(nr_S[1:3]) > 23:
            nr_S = input("Cifrele 2 si 3 tr sa fie < 24: ")
    # print(nr)
    # print(int(nr_S[1:3]))
    return nr_S

# def validare_AA(nr_An):
#     # validare_input_numar(nr_An)
#     # print("Cifrele 2 si 3: ",int(nr_An[1:3]))
#     while int(nr_An[1:3]) > 23:
#         nr_An = input("Cifrele 2 si 3 tr sa fie < 24: ")
#     return nr_An


def validare_input_numar(nr):
    for i in range(len(nr)):
        # print(list(nr[0]))
        if str(nr).isdigit() is False:
            nr = input("Introdu doar cifre: ")
        elif len(nr) != 13:
            nr = input("Introdu 13 cifre: ")

    # for j in list(nr):
    #     print(j)
    #

    # if list(nr) > str(23):
    #     nr = input("Cifrele 2 si 3 tr sa fie < 24: ")
    return nr


def input_CNP():
    # validare_S(nr)
    # validare_AA(nr)
    return validare_input_numar(input("Introdu CNP-ul format din 13 cifre: "))

def calcul():
    cnp = input_CNP()
    validare_S(cnp)
    # validare_AA(cnp)
    return cnp
# c=input_CNP()
# print(c)
calcul()

# Valideaza S
