# 1
# x = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'a': 4,
#     'd': 5
# }
# print(x['a'])

# 2
# def a(parametru):
#     parametru[2] = 'f'
#     return parametru
#
#
# x = {
#     1: 'a',
#     2: 'b',
#     3: 'c'
# }
#
# y = a(x)
# print(y)


# 3
# def functie1(lista_cuvinte):
#     lista = []
#     for n in lista_cuvinte:
#         lista.append((len(n), n))
# return lista
# return lista[-1][0], lista[-1][1]
# print('print')
# lista.sort()


# rezultat, rezultat1 = functie1(['pip', 'Exercitiu', 'Python'])
# rezultat = functie1(['pip', 'Exercitiu', 'Python'])
# print(rezultat)
# print(rezultat1)

# 4


# def functie(lista):
#     item = 1
#     for x, y in enumerate(lista):
#         item *= x
#         return lista[y+1]
#
#
# lista = [1, 2, 3]
# print(functie(lista))


# 5
#
# my_tuple = (1, 10, 100)
# t2 = my_tuple * 4
# print(t2)
# print(len(t2))


# 6

# def functie1():
#     # print("Variabila este definita", var)
#     return f"Variabila este definita {var}"
#
#
# var = 30
# print(functie1())
# print(var)


# 7

# x = 10
# while x > 1:
#     x -= 1
#     continue
#
# print(x)


# 8

# x = ['ab', 'cd', 'ed']
# for i, j in enumerate(x):
#      x[i] = j.title()
#
# print(x)


# 9

# lista1 = list(set([1, 3, 4, 3, 5, 6]))
# lista1 = set([1, 3, 4, 3, 5, 6, 7, 8, 7])
# print(lista1)
# lista1 = list(lista1)
# print(lista1)
# del lista1[0:5]
# print(lista1)


# 10
# cuvant = "cu'va\\'nt"
# cuvant = "cu'va\"nt"
# print(cuvant)
# print(cuvant[::-1])


# 11

# def functie():
#     l = list() # l = []
#     # for i in range(1, 4, 2):
#     for i in range(1, 4, 2):
#         l.append(i**2)
#     print(l)
#
# functie()


# 12
# def a(*args):
#     return args
#
#
# s = a(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(s)

# 13
# a = {1: 'a', 2: 'b', 3: 'c'}
# b = {2: 'd', 3: 'e', 4: 'f'}
# print({**a})
# c = {**a, **b}
# print(c)


# 14
# dictionar = {"pisica": "pisica1", "caine": "caine1", "cal": "cal1"}
# dictionar = {"caine": "caine1", "cal": "cal1"}
# dictionar['pisica'] = 'pisica2'
# print(dictionar)

# nr = '279146358279'
# cnp = '1781115293145'
# list_nr = list(nr)
# list_cnp = list(cnp)
# c = []
# for i in range(0, len(list_nr)):
#     c.append(int(list_nr[i]) * int(list_cnp[i]))
# c = [int(nr[i]) * int(cnp[i]) for i in range(0, len(list(nr)))]
# s = 0
# # for j in c:
# #     s = s + int(j)
# for j in c: s = s + int(j)
# print(c)
# print(s)
# print(s / 11)
# print(s % 11)

# calculare cu nr de control
# def nr_control_validation(cnp):
#     nr_control = '279146358279'
#     list_multiplication = [int(nr_control[i]) * int(cnp[i]) for i in range(0, len(list(nr_control)))]
#     sum_control = 0
#     for j in list_multiplication:
#         sum_control = sum_control + int(j)
#     return sum_control % 11
#
# print(nr_control_validation('1781111529316'))

# calculare an bisect
# def leap_year():
#     year = input("Introdu anul: ")
#     while True:
#         if int(year) % 4 == 0:
#             print(f"Anul {(year)} este bisect")
#         elif int(year) % 100 == 0 and int(year) % 400 == 0:
#             print(f"Anul {(year)} este bisect")
#         else:
#             print(f"Anul {(year)} este normal")
#         break
#     return
#
# leap_year()


# afisare intr-o lista ani bisecti
# def list_leap_years(list):
#     leap_years = []
#     for i in list:
#         if ((int(i) % 4 == 0 and int(i) % 100 != 0) or int(i) % 400 == 0):
#             leap_years.append(i)
#     return leap_years
#
# list = range(1800, 2100)
# list1 = range(1800, 2100)
# lst_leap_years = [i for i in list1 if ((int(i) % 4 == 0 and int(i) % 100 != 0) or int(i) % 400 == 0)]
#
# print(list_leap_years(list))
# print(lst_leap_years)

# verificare data
list_LL = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
list_ZZ = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
           '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
           '25', '26', '27', '28', '29', '30', '31']
import datetime
def verificare(an, luna, zi):
    print(str(datetime.datetime(int(an), int(luna), int(zi))))
    try:
        datetime.datetime(int(an), int(luna), int(zi))
        return True
    except ValueError:
        # print(datetime.datetime(int(an), int(luna), int(zi)))
        return False


list_century_20 = list(range(1900,2000))
print(f" list_century_20)
data = "000228"
data_i = datetime.datetime(1901,1,1)
data_s = datetime.datetime(1901,12,31)
print(data_i.strftime('%y%m%d'))
r = []
for n in range(int((data_s-data_i).days)):
    r.append(data_i+datetime.timedelta(n))

# print("Range:", r)
# data_r = list(range(data_i, data_s))
print(f'{list_century_20:03d}')
# print(data_s.strptime("%y"))
# if verificare(8, 3, 16) is True:
#
#     print("Data este corecta")
# else:
#     print("Data este gresita")

print(verificare(1800, 2, 27))
# datetime.datetime.year
# print(datetime.datetime.strptime(data, "%y"))

# def find_century(year):
#     # No negative value is allow for year
#     if (year <= 0):
#         print("0 and negative is not allow for a year")
#
#     # If year is between 1 to 100 it
#     # will come in 1st century
#     elif (year <= 100):
#         print("1st century")
#     elif (year % 100 == 0):
#         print(year // 100, "century")
#     else:
#         print(year // 100 + 1, "century")
#
#
# # Driver code
# year = 1820
# find_century(year)