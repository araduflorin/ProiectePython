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
        tasks = csv.reader(file)
        for task in tasks:
            list_tasks.append(task)
        #     print(row[0])
        # print(list_tasks)
    return list_tasks

def add_tasks():
    while True:
        with open('tasks.csv', mode='a', newline='') as file:
            # exit_opt = input('Continuati adaugarea? (d\\n)')
            # if exit_opt == 'd':
                list_add_tasks = csv_reader_tasks()
                list_categories = csv_reader_categories()
                # for index, row in enumerate(list_add_tasks):
                    # print(row)
                print(sorted(list_add_tasks, key=lambda cat: cat[3]))
                # list_sorted_by_category = sorted(list_add_tasks, key=lambda cat: list_add_tasks(row[3]), reverse=True)
                check_tasks = []
                for index, row in enumerate(list_add_tasks):
                    check_tasks.append(row[0])
                print('Check task:', check_tasks)

                list_check_category = [cat for lst_cat in list_categories for cat in lst_cat]
                print(list_check_category)
                var_task = input("Adauga un task: ").lower()
                var_date = input("Adauga data: ").lower()
                var_person = input("Adauga persoana responsabila: ").lower()
                var_category = input("Adauga categoria: ").lower()
                list_tasks = [var_task, var_date, var_person, var_category]

                if var_task not in check_tasks:
                    if var_category in list_check_category:
                        writer = csv.writer(file)
                        writer.writerow(list_tasks)
                        exit_opt = input('Continuati adaugarea? (d\\n)')
                        if exit_opt == 'd':
                            continue
                        elif exit_opt == 'n':
                            break
                    else:
                        print('Categoria nu exista!')
                        continue
                else:
                    print('Task-ul exista deja!')
                    continue
            # elif exit_opt == 'n':
            #     break
    return

def sort_category():
    sort_tasks = csv_reader_tasks()
    for index, row in enumerate(sort_tasks):
        # print(sorted(sort_tasks, key=lambda cat: (row[3]), reverse=True))
            print(row.sort(key=lambda cat: row))
    # print(sorted(sort_tasks, key=lambda cat: cat[3]))
    return

def main_function():
    while True:
        # add_categories()
        add_tasks()
        exit_program = input('Daca vrei sa iesi, apasa \'x\', altfel apasa alta tasta: ').lower()
        if exit_program == 'x':
            break
    return

def menu():
    while True:
        # print('Alege una din urmatoarele optiuni:')
        list_option = input('Alege una din urmatoarele optiuni: \n Pentru listare apasa tasta 1'
                            '\n Pentru sortare apasa tasta 2 \n Pentru filtrare date apasa tasta 3'
                            '\n Pentru adaugare task nou apasa tasta 4 \n Pentru editare task existent apasa tasta 5'
                            '\n Pentru stergere task existent apasa tasta 6 '
                            '\n Pentru iesire din programa apasa \'x\' \n Alege optiunea: ')
        if list_option == '1':
            print('Ati apasat tasta 1!')
        elif list_option == '2':
            list_sort = input('Pentru sortare alege una din optiunile: \n a) sortare ascendenta task: '
                              '\n b) sortare descendenta task: \n c) sortare ascendenta data: \n d) sortare descendenta data: '
                              '\n e) sortare ascendenta persoana responsabila: \n f) sortare descendenta persoana responsabila:'
                              '\n g) sortare ascendenta categorie: \n h) sortare descendenta categorie: '
                              '\n Alege o litera pentru sortare: ' )
            if list_sort == 'a':
                print('Ati apasat tasta a!')
            elif list_sort == 'b':
                print('Ati apasat tasta b!')
            elif list_sort == 'c':
                print('Ati apasat tasta c!')

        elif list_option == '3':
            print('Ati apasat tasta 3!')
            filter_option = input('Filtrarea se face dupa:\n'
                                  'a) Task\n'
                                  'b) Data\n'
                                  'c) Persoana responsabila\n'
                                  'd) Categorie\n'
                                  'Alege optiunea: ')
            if filter_option == 'a':
                print('Ati ales filtrarea dupa Task!')
            elif filter_option == 'b':
                print('Ati ales filtrarea dupa Data!')
            elif filter_option == 'c':
                print('Ati ales filtrarea dupa Persoana responsabila!')
            elif filter_option == 'd':
                print('Ati ales filtrarea dupa Categorie!')
        elif list_option == '4':
            print('Adaugati un task nou!')
            add_tasks()
        elif list_option == '5':
            print('Ati apasat tasta 5!')
        elif list_option == '6':
            print('Ati apasat tasta 6!')
        elif list_option == 'x':
            break
    return


# menu()
# main_function()
# add_tasks()
sort_category()