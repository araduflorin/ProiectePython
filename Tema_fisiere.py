import csv

def csv_reader_categories():
    list_categories = []
    with open('categories.csv','r+') as file:
        categories = csv.reader(file)
        for item in categories:
            list_categories.append(item)
    return list_categories

def add_categories():
    with open('categories.csv', mode='a', newline='') as file:
        list_add_categories = csv_reader_categories()
        print(list_add_categories)
        var_category = input("Adauga o noua categorie: ").lower()
        list_categories_new = [i[0].lower() for i in list_add_categories]
        if var_category not in list_categories_new:
            writer = csv.writer(file)
            writer.writerow([var_category])
        else:
            print('Eelementul exiat deja')
    return

def csv_reader_tasks():
    list_tasks = []
    with open('tasks.csv','r+') as file:
        categories = csv.reader(file)
        for index, row in enumerate(categories):
            list_tasks.append(row)
            print(row[0])
        # print(list_tasks)
    return list_tasks

def add_tasks():
    with open('tasks.csv', mode='a', newline='') as file:
        list_add_tasks = csv_reader_tasks()
        print(list_add_tasks)
        # l = [list_add_tasks[0]]
        # print(l)
        # l = [i for i in list_add_tasks]
        # print(l)
        # print(list_add_tasks[0][0])
        var_task = input("Adauga un task: ").lower()
        var_date = input("Adauga data: ").lower()
        var_person = input("Adauga persoana responsabila: ").lower()
        var_category = input("Adauga categoria: ").lower()
        list_tasks = [var_task, var_date, var_person, var_category]
        # list_tasks_new = [i[0].lower() for i in list_add_tasks]
        # print(list_add_tasks[0])
        if var_task not in list_add_tasks[0][0]:
            writer = csv.writer(file)
            writer.writerow(list_tasks)
        else:
            print('Eelementul exiat deja')
    return

def main_function():
    while True:
        # add_categories()
        add_tasks()
        exit_program = input('Daca vrei sa iesi, apasa \'x\', altfel apasa alta tasta: ').lower()
        if exit_program == 'x':
            break
    return

main_function()