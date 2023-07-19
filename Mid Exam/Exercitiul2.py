
while True:
    n = input("Introduceti nr. de secunde: ")
    if n.isdigit() is False:
        print("Introdu un nr intreg:")
    else:
        n = int(n) % (24 * 3600)
        nr_ore = n // 3600
        print("Ore: ", nr_ore)
        n = n % 3600
        nr_min = n // 60
        print("Minute:", nr_min)
        nr_sec = n % 60
        print("Secunde: ", nr_sec)


