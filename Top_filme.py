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
d = {}
for el in lista_filme:
    # e = [len(el.get("filme"))]
    e = len(el.get("filme"))
    n = el.get("nume")
    # d[n]=e
    print(n,e)
# n=max(d , key=d.get)
print("Utilizatorul cu cele mai multe filme vizionate este: ", n)

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
dict_film = {}
for film in lst_film:
    if film in dict_film:
        dict_film[film] += 1
    else:
        dict_film[film] = 1
print(dict_film)
m = max(dict_film, key=dict_film.get)
print("Cel mai vizionat film este ", m)
for el,c in sorted(dict_film.items()):
    if c >=1:
        print(f"{el} este vizionat de {c} ori")
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
s=sorted(count_dict.items())
print(s)
# for element, count in count_dict.items():
for element, count in sorted(count_dict.items()):

    # if count >= 1:
        print(f"{element} appears {count} times in the list.")
