
def inmultire(a,b):
    return a * b
def impartire(a,b):
    while b == 0:
        b = int(validare_inpt_numar(input('Introduceti o cifra diferita de 0: ')))
    return a / b
def adunare(a,b):
    return a + b
def scadere(a,b):
    return a - b
def input_user_cifre():
    return int(validare_inpt_numar(input('Introdu cifra 1: '))), int(validare_inpt_numar(input('Introdu cifra 2: ')))
def validare_inpt_numar(par1):
    while str(par1).isdigit() is False:
        par1 = input('Introdu o cifra: ')
    return par1
def operator():
    var_input = input('Alege operatorul: ')
    while var_input not in ["+","-","/","*"]:
        var_input = input('Alege un operator corect: -, +, *, /: ')
    return var_input
def calcul():
    operator_ales = operator()
    a, b = input_user_cifre()
    if operator_ales == '+':
        return adunare(a, b)
    elif operator_ales == '-':
        return scadere(a, b)
    elif operator_ales == '*':
        return inmultire(a, b)
    elif operator_ales == '/':
        return impartire(a, b)
def metoda_principala():
    while True:
        print(calcul())
        iesire_program = input('Vrei sa iesi, introdu \'x\': ').lower()
        if iesire_program == 'x':
            break

metoda_principala()