import csv


def csv_reader():
    list_elements_read = []
    with open('categories.csv','r+') as file:
        categories = csv.reader(file)
        for item in categories:
            list_elements_read.append(item)
    return list_elements_read


with open('categories.csv', mode='a', newline='') as file:
    list_elements = csv_reader()
    print(list_elements)
    # writer = csv.writer(file)
    var_category = input("Adauga o noua categorie: ").lower()
    list_elements_new = [i[0].lower() for i in list_elements]
    while True:
        if var_category not in list_elements_new:
            writer = csv.writer(file)
            writer.writerow([var_category])
        # print(list_elements_new)
        else:
            print('Categoria exista deja')
            iesire_program = input('Vrei sa iesi, introdu \'x\': ').lower()
            if iesire_program == 'x':
                break
