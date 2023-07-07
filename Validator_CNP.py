import datetime

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

def date_validation(an, luna, zi):
    date_start = datetime.datetime.strptime("1800-1-1", "%Y-%m-%d")
    date_end = datetime.datetime.strptime("2100-1-1", "%Y-%m-%d")
    day_delta = datetime.timedelta(days=1)
    date_range = date_end - date_start
    list_date = []
    for d in range(date_range.days):
        date_all = date_start + d * day_delta
        list_date.append(date_all.strftime("%Ey%m%d"))
    data_check = str(an) + str(luna) + str(zi)
    if data_check in list_date:
        return True
    elif data_check not in list_date:
        return False


def number_validate():
    nr = input("Introduceti CNP-ul format din 13 cifre: ")
    while True:
        if nr.strip().isdigit() is False:
            nr = input("Introduceti doar cifre: ")
            continue
        if len(nr) != 13:
            nr = input("Introduceti 13 cifre: ")
            continue
        if (nr[0]) == '0':
            nr = input(f"Prima cifra ({nr[0]}) trebuie sa fie intre 1 si 9: ")
            continue
        if date_validation(nr[1:3], nr[3:5], nr[5:7]) is False:
            nr = input(f"Data nasterii (an,luna,zi) formata din cifrele de la 2 la 7 ({nr[1:7]}) nu este valida: ")
            continue
        if (nr[7:9]) not in list_JJ:
            nr = input(
                f"Nr. format din cifrele 8 si 9 ({nr[7:9]}), judetul, tb. sa fie cuprinse in intervalele 01-46 si 51-52: ")
            continue
        if (nr[9:12]) == '000':
            nr = input(
                f"Nr. format din cifrele 10, 11 si 12 ({nr[9:12]}) tb. sa fie un nr cuprins in intervalul 001-999: ")
            continue
        if int(nr[12]) != nr_control_validation(nr):
            nr = input(f"Cifra 13 ({nr[12]}) nu este valida. Trebuie sa fie {nr_control_validation(nr)} : ")
            continue
        print(f"CNP-ul {nr} este valid!")
        break
    return


number_validate()
