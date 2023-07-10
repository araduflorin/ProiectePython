import csv


def csv_reader():
    list_elements = []
    with open('categorii.csv','r+') as file:
        categorie = csv.reader(file)
        for item in categorie:
            list_elements.append(item)
    return list_elements


with open('categorii.csv', mode='a', newline='') as file:
    list_elements = csv_reader()
    print(list_elements)
    # writer = csv.writer(file)
    var_categorie = input("Adauga un nou element: ").lower()
    list_elements_new = [i[0].lower() for i in list_elements]
    if var_categorie not in list_elements_new:
        writer = csv.writer(file)
        writer.writerow(var_categorie)
    # print(list_elements_new)
    else:
        print('elementul exista deja')

