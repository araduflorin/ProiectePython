
while True:
    n = input("Introduceti un nr. intreg: ")
    if n.isdigit() is False:
        print("Nr. nu este valid:")
        continue
    elif int(n) % 2 == 0:
        print("Nr. este par!")
        continue
    elif int(n) % 2 != 0:
        print("Nr. este impar!")
        continue
    break
