while True:
     nr = int(input("Intoduceti un nr intreg: "))
     if (nr % 3 == 0) and (nr % 5 == 0):
         print("FizzBuzz")
     elif nr % 3 == 0:
         print("Fizz")
     elif nr % 5 == 0:
         print("Buzz")
     else:
         print(nr)