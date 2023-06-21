lista_filme_utilizatori = [{'nume': 'George', 'filme': ['Shrek', 'Bond', 'Fight Club']},
                           {'nume': 'Cristian', 'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']},
                           {'nume': 'Stefan', 'filme': ['Fight Club', 'Slumdog Milionare']}]

lista_filme = lista_filme_utilizatori[0]["filme"] + lista_filme_utilizatori[1]["filme"] + lista_filme_utilizatori[2][
    "filme"]
# --------------------------creare dictionar nesortat cu formatul {utilizator:nr_de_filme_vizionate}
nume_utilizatori = {}
for el in lista_filme_utilizatori:
    # e = [len(el.get("filme"))]
    # e = len(el.get("filme"))
    e = len(el.get("filme"))
    n = el.get("nume")
    nume_utilizatori[n] = e
# --------------------------creare dictionar sortat cu formatul {utilizator:nr_de_filme_vizionate}
sort_nume_utilizatori = {}
sortare_val_utilizatori = sorted(nume_utilizatori, key=nume_utilizatori.get, reverse=True)
for n in sortare_val_utilizatori:
    sort_nume_utilizatori[n] = nume_utilizatori[n]

# --------------------------creare dictionar nesortat cu formatul {film:nr_de_vizionari}
nr_filme = {}
for f in lista_filme:
    if f in nr_filme:
        nr_filme[f] += 1
    else:
        nr_filme[f] = 1

# ----------------------------creare dictionar sortat cu formatul {film:nr_de_vizionari}
sortare_vizionari = {}
sortare_valoare = sorted(nr_filme, key=nr_filme.get, reverse=True)
for k in sortare_valoare:
    sortare_vizionari[k] = nr_filme[k]

u = list(sort_nume_utilizatori.keys())[0]
print("----------------------")
print("Utilizatorul cu cele mai multe filme vizionate este:", u)

m = list(sortare_vizionari.keys())[0]
print("----------------------")
print("Cel mai vizionat film este:", m)

# ------------------------------top filme
print("-------Top filme-------")
for k, v in sortare_vizionari.items():
    print(f"{k} este vizionat de {v} ori")

# ---------------------------top utilizatori
print("-------Top utilizatori-------")
for k, v in sort_nume_utilizatori.items():
    print(f"{k} a vizionat {v} filme")
# -------------------------------------------------------------------------------
