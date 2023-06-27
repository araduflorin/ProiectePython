CNP = {'S': 0, 'AA': 0, 'LL': 0, 'ZZ': 0, 'JJ': 0, 'NNN': 0, 'C': 0}

# ------------------
# Introdu CNP-ul
while True:
    CNP_user = input("Introdu CNP-ul format din 13 cifre: ")
    if len(CNP_user) != 13:
        print("Nu ati introdus 13 cifre")
        continue
    else:
        CNP_user = list(CNP_user)
        for c in CNP_user:


        # S_user = input("Indrodu S-ul: ")
        # CNP['S'] = int(S_user)
        print(CNP_user)
# l=[]
# for v, k in enumerate(CNP.items()):
#     l[v]=k
#     # print(list(str(k)))
# print(l)

# Valideaza S
