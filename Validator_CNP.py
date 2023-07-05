
list_S = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
list_LL = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
list_ZZ = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
           '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
           '25', '26', '27', '28', '29', '30', '31']
list_JJ = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
           '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
           '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36',
           '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '51', '52']

def nr_control_validation(cnp):
    nr_control = '279146358279'
    list_multiplication = [int(nr_control[i]) * int(cnp[i]) for i in range(0, len(list(nr_control)))]
    sum_control = 0
    for j in list_multiplication:
        sum_control = sum_control + int(j)
    return sum_control % 11

def number_validate():
    nr = input("Introdu CNP-ul format din 13 cifre: ")
    while True:
        if nr.strip().isdigit() is False:
            # print(type(nr))
            # print(nr.isdigit())
            # if str(nr).isdigit() is False:
            nr = input("Introduceti doar cifre: ")
            continue
        if len(nr) != 13:
            nr = input("Introduceti 13 cifre: ")
            continue

        if (nr[0]) not in list_S:
            nr = input(f"Prima cifra ({nr[0]}) trebuie sa fie intre 1 si 9: ")
            continue
        if (nr[0]) in ['5', '6'] and int(nr[1:3]) > 23:
            nr = input(f"Nr. format din cifrele 2 si 3 ({nr[1:3]}) tr sa fie < 24: ")
            continue
        if (nr[3:5]) not in list_LL:
            nr = input(f"Nr. format din cifrele 4 si 5 ({nr[3:5]}), luna, tb. sa fie cuprinse in intevalul 01-12: ")
            continue
        if (nr[5:7]) not in list_ZZ:
            nr = input(f"Nr. format din cifrele 6 si 7 ({nr[5:7]}), ziua, tb. sa fie cuprinse in intevalul 01-31: ")
            continue
        if (nr[7:9]) not in list_JJ:
            nr = input(f"Nr. format din cifrele 8 si 9 ({nr[7:9]}), judetul, tb. sa fie cuprinse in intervalele 01-46 si 51-52: ")
            continue
        if (nr[9:12]) == '000':
            nr = input(f"Nr. format din cifrele 10, 11 si 12 ({nr[9:12]}) tb. sa fie un nr cuprins in intervalul 001-999: ")
            continue
        if int(nr[12]) != nr_control_validation(nr):
            nr = input(f"Cifra 13 nu este valida. Trebuie sa fie {nr_control_validation(nr)} : ")
            continue
        print(f"CNP-ul {nr} este valid!")
        break
    return

number_validate()
