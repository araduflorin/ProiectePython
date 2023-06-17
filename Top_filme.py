# d1 = {'nume': 'George', 'filme': ['Shrek', 'Bond', 'Fight Club'] }
# d2 = { 'nume' : 'Cristian', 'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']}
# d3 = { 'nume' : 'Stefan', 'filme': ['Fight Club', 'Slumdog Milionare'] }
# v = [ d1, d2, d3 ]

lista_filme = [ { 'nume': 'George', 'filme': ['Shrek', 'Bond', 'Fight Club'] },
{ 'nume' : 'Cristian', 'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']},
{ 'nume' : 'Stefan', 'filme': ['Fight Club', 'Slumdog Milionare']}]
a = lista_filme[0]["filme"]
b = lista_filme[1]["filme"]
c = lista_filme[2]["filme"]
# print(type(a))
lst_film = a + b + c
# print("Nr de filme vazute", lista_filme[0].count["filme"])
count = {}
for f in lst_film:
    # if f in count:
    #     count[f] += 1
    # else:
    #     count[f] = 1
    count[i]
print(count)
for i,j in count.items():
#    if j > 0:
        print(f"{i} a fost vizionat de {j} ori")
print(lst_film)

lst_nume = lista_filme[0]["nume"] + lista_filme[1]["nume"] + lista_filme[2]["nume"]
print(lst_nume)
# my_list = ['a', 'b', 'c', 'a', 'd', 'e', 'b', 'a']
# count_dict = {}
#
# # loop through the list and count occurrences of each element
# for element in my_list:
#     if element in count_dict:
#         count_dict[element] += 1
#     else:
#         count_dict[element] = 1
#
# print(count_dict)
# for element, count in count_dict.items():
#     if count > 1:
#         print(f"{element} appears {count} times in the list.")