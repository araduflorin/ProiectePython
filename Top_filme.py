
lista_filme = [{'nume': 'George', 'filme': ['Shrek', 'Bond', 'Fight Club']},
               {'nume': 'Cristian', 'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']},
               {'nume': 'Stefan', 'filme': ['Fight Club', 'Slumdog Milionare']}]

filme=[]
for i, v in enumerate(lista_filme[0]['filme']):
    filme.append(v)

for i, v in enumerate(lista_filme[1]['filme']):
    filme.append(v)

for i, v in enumerate(lista_filme[2]['filme']):
    filme.append(v)

filme_adunate=[]
for i in filme:
    count_filme=filme.count(i)
    filme_adunate.append((count_filme,i))

unice = set(filme_adunate)
lista_unice = list(unice)
lista_unice.sort()
print("Cel mai vizionat film este:",lista_unice[-1][1])

# -------------------------------------------
list_users = []
for i in lista_filme:
    n = i.get("nume")
    f = len(i.get("filme"))
    list_users.append((f,n))
list_users.sort()
print("Utilizatorul cu cele mai multe filme vizionate: ", list_users[-1][1])

#-------------------------------------------

print("------------Top utilizatori------------")
list_users_top = list_users[::-1]
for i, j in enumerate(list_users_top):
    print(f"{j[1]} a vizionat {j[0]} filme")

# -------------------------------------------
print("------------Top filme------------")
lista_filme_top = lista_unice[::-1]
for i, j in enumerate(lista_filme_top):
    print(f"Filmul {j[1]} a fost vizionat {j[0]} ori")


