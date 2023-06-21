# d1 = {'nume': 'George', 'filme': ['Shrek', 'Bond', 'Fight Club'] }
# d2 = { 'nume' : 'Cristian', 'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']}
# d3 = { 'nume' : 'Stefan', 'filme': ['Fight Club', 'Slumdog Milionare'] }
# v = [ d1, d2, d3 ]
import operator

lista_filme = [{'nume': 'George', 'filme': ['Shrek', 'Bond', 'Fight Club']},
               {'nume': 'Cristian', 'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']},
               {'nume': 'Stefan', 'filme': ['Fight Club', 'Slumdog Milionare']}]
# print(len(lista_filme[0]["filme"]))
# print(lista_filme.sort(key=operator.itemgetter("filme") ))
sort_film = {}
# l = lista_filme.e
nume_utilizatori= {}
for el in lista_filme:
    # e = [len(el.get("filme"))]
    # e = len(el.get("filme"))
    e = len(el.get("filme"))
    n = el.get("nume")
    nume_utilizatori = {n: e}
    print("Nume utilizatori: ",nume_utilizatori)

sort_nume_utilizatori = {}
sortare_val_utilizatori = sorted(nume_utilizatori, key=nume_utilizatori.get, reverse=True)
for n in sortare_val_utilizatori:
    sort_nume_utilizatori[n] = nume_utilizatori[n]
    # print("Utilizatori sortati: ",sort_nume_utilizatori)

# for f in d.items():
#     print(f)
# n=max(d , key=d.get)
print("Utilizatorul cu cele mai multe filme vizionate este: ", e)

# for i, j in enumerate(lista_filme):
#      for v in j.get("filme"):
#        print(v)
# print(v.count(i.values()))
# print(lista_filme[i])
# print(lista_filme[0]["filme"] + lista_filme[1]["filme"])
lst_film = lista_filme[0]["filme"] + lista_filme[1]["filme"] + lista_filme[2]["filme"]

# for i in lst_film:
#      d = {i:lst_film.count(i)}
# lst_film.sort()
# d = {i:lst_film.count(i) for i in sorted(lst_film)}

# print(sorted(d.items()))
# print(d)
# print(type(lst_film))
dict_film = {}  # creare dictionar cu formatul {film:nr_de_vizionari}
for film in lst_film:
    if film in dict_film:
        dict_film[film] += 1
    else:
        dict_film[film] = 1
print("Lista filmelor: ", dict_film)

# --------------------------------------------------------------------------------
sortare_vizionari = {} # creare dictionar sortat cu formatul {film:nr_de_vizionari}
sortare_valoare = sorted(dict_film, key=dict_film.get, reverse=True)
for k in sortare_valoare:
    sortare_vizionari[k] = dict_film[k]
print("Vizionari sortate: ", sortare_vizionari)
print(sortare_vizionari.items())
for el, c in sortare_vizionari.items():
    # print(el,c)
    print(f"{el} este vizionat de {c} ori")
# -------------------------------------------------------------------------------
# m = max(dict_film, key=dict_film.get)  # cel mai vizionat film
m = list(sortare_vizionari.keys())[0]
print("Cel mai vizionat film este >>>> ", m)
# sort_dict = sorted({(n, film) for (film, n) in dict_film.items()})

# print("Lista sortata: ",sort_dict)
# for film, n in sort_dict:
# sort_dict = dict(sorted((n, film) for (film, n ) in dict_film.items()))

# if n >= 1:
#     print(f"{n} appears {film} times in the list.")
# print(sort_dict)
#      print(set(lst_film.count(f)))
#         count[f] += 1
#     else:
#         count[f] = 1
# print(count)
# for i,j in count.items():
# #    if j > 0:
#         print(f"{i} a fost vizionat de {j} ori")
print(lst_film)

my_list = ['b', 'd', 'c', 'd', 'd', 'e', 'b', 'a']
count_dict = {}

# loop through the list and count occurrences of each element
for element in my_list:
    if element in count_dict:
        count_dict[element] += 1
    else:
        count_dict[element] = 1
# s=sorted(count_dict.items())
# print(s)
# for element, count in count_dict.items():
sort_dict = {}
sort_key = sorted(count_dict, key=count_dict.get, reverse=True)
for w in sort_key:
    sort_dict[w] = count_dict[w]
print("Lista sortata: ", sort_dict)

for element, count in sort_dict.items():
    # if count >= 1:
    print(f"{element} appears {count} times in the list.")
