CNP = {'S': [], 'AA': 0, 'LL': 0, 'ZZ': 0, 'JJ': 0, 'NNN': 0, 'C': 0}
list_S = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
list_LL = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
list_ZZ = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
           '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
           '25', '26', '27', '28', '29', '30', '31']
list_JJ = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
           '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
           '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36',
           '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '51', '52']
# list_NNN = []
# for i in range(1, 1000):
#     list_NNN.append('{0:03}'.format(i))
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
        if (nr[5:7]) not in list_ZZ:
            nr = input("Cifrele 6 si 7 (ziua) tb. sa fie cuprinse in intevalul 01-31: ")
            continue
        if (nr[7:9]) not in list_JJ:
            nr = input("Cifrele 8 si 9 (judetul) tb. sa fie cuprinse in intervalele 01-46 si 51-52: ")
            continue
        if (nr[9:12]) == '000':
            nr = input("Cifrele 10, 11 si 12 tb. sa fie un nr cuprins in intervalul 001-999: ")
            continue
        break
    return nr


def input_CNP():

    return number_validate(input("Introdu CNP-ul format din 13 cifre: "))


def calcul():
    cnp = input_CNP()
    number_validate(cnp)

    return cnp


# nr = '279146358279'
# cnp = '178111529314'
# list_nr = list(nr)
# list_cnp = list(cnp)
# c = []
# for i in range(0, len(list_nr)):
#     c.append(int(list_nr[i]) * int(list_cnp[i]))
# s = 0
# for j in c:
#     s = s + int(j)
#
# print(c)
# print(s)

print(calcul())


