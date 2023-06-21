lista_filme_utilizatori = [{'nume': 'George', 'filme': ['Shrek', 'Bond', 'Fight Club']},
                           {'nume': 'Cristian', 'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']},
                           {'nume': 'Stefan', 'filme': ['Fight Club', 'Slumdog Milionare']}]

lista_filme = lista_filme_utilizatori[0]["filme"] + lista_filme_utilizatori[1]["filme"] + lista_filme_utilizatori[2][
    "filme"]
print(lista_filme)

nr_filme = {}
for f in lista_filme:
    if f in nr_filme:
        nr_filme[f] += 1
    else:
        nr_filme[f] = 1

print(nr_filme)

m = list(nr_filme.values()).sort()
print(m)