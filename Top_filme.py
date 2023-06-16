
# while True:
#       nr = int(input("Intoduceti un nr intreg: "))
#       if nr % 3 == 0:
#          print("Fizz")
#          #break
#       elif nr % 5 == 0:
#          print("Buzz")
#          #break
#       elif (nr % 3 == 0) and (nr % 5 == 0):
#          print("FizzBuzz")
#          #break
#       else:
#          print(nr)


# nr = int(input("Intoduceti un nr intreg: "))

# while True:
#     nr = int(input("Intoduceti un nr intreg: "))
#     if (nr % 3 == 0) and (nr % 5 == 0):
#         print("FizzBuzz")
#     elif nr % 3 == 0:
#         print("Fizz")
#     elif nr % 5 == 0:
#         print("Buzz")
#     else:
#         print(nr)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    if i in b:
        c.append(i)
print(list(set(c)))


# print(set(a))
# print(set(b))
