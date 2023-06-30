CNP = {'S': [], 'AA': 0, 'LL': 0, 'ZZ': 0, 'JJ': 0, 'NNN': 0, 'C': 0}
list_S = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
list_LL = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
AA = []


def number_validate(nr):
    # print((nr[3:5]))
    while True:
        if str(nr).isdigit() is False:
            # if str(nr).isdigit() is False:
            nr = input("Introdu doar cifre: ")
            continue
        if len(nr) != 13:
            nr = input("Introdu 13 cifre: ")
            continue
        if (nr[0]) not in list_S:
            nr = input("Prima cifra trebuie sa fie intre 1 si 9: ")
            continue
        if (nr[0]) in ['5', '6'] and int(nr[1:3]) > 23:
            nr = input("Cifrele 2 si 3 tr sa fie < 24: ")
            continue
        if (nr[3:5]) not in list_LL:
            nr = input("Cifrele 4 si 5 (luna) tb. sa fie cuprinse in intevalul 01-12: ")
            continue
        break
    return nr


# def length_validate(nr_length):
#     while len(nr_length) != 13:
#         nr_length = input("Introdu 13 cifre: ")
#     return nr_length


def input_CNP():
    # validare_S(nr)
    # validare_AA(nr)
    return number_validate(input("Introdu CNP-ul format din 13 cifre: "))


def calcul():
    cnp = input_CNP()
    number_validate(cnp)
    # length_validate(cnp)
    # validate_S(cnp)
    # validate_AA(cnp)
    # validare_S(cnp)
    # validare_AA(cnp)
    return cnp


# c=input_CNP()
# print(c)
print(calcul())

# Valideaza S
