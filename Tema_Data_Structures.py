initial_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
list_ord_asc = sorted(initial_list)
list_ord_desc = sorted(initial_list, reverse=True)
list_even = list_ord_asc[1::2]
list_odd = list_ord_asc[::2]
list_x3 = list_ord_asc[2::3]
print("Lista initiala: ", initial_list)
print("Lista ordonata ascendent: ", list_ord_asc)
print("Lista ordonata ascendent: ", list_ord_desc)
print("Lista nr. pare: ", list_even)
print("Lista nr. impare: ", list_odd)
print("Lista multipli ai nr. 3: ", list_x3)