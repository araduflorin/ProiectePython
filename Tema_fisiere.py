import csv

def csv_reader(file_to_read):
    list_elements_read = []
    with open(file_to_read,'r+') as file:
        categories = csv.reader(file)
        for item in categories:
            list_elements_read.append(item)
    return list_elements_read

def add_categories():
    with open('categories.csv', mode='a', newline='') as file:
        list_elements = csv_reader('categories.csv')
        print(list_elements)
        var_category = input("Adauga o noua categorie: ").lower()
        list_elements_new = [i[0].lower() for i in list_elements]
        if var_category not in list_elements_new:
            writer = csv.writer(file)
            writer.writerow([var_category])
        else:
            print('Eelementul exiat deja')
    return

def main_function():
    while True:
        add_categories()
        exit_program = input('Daca vrei sa iesi, apasa \'x\', altfel apasa alta tasta: ').lower()
        if exit_program == 'x':
            break
    return

main_function()