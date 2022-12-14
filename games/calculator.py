user = str(input('Operations first alphabet kodi: '))
value_1 = float(input('Sir ondh value kodi: '))
value_2 = float(input('Sir innondh value kodi: '))


def add(value_1, value_2):
    add = value_1 + value_2
    print(add)

def subract(value_1, value_2):
    subract = value_1 - value_2
    print(subract)

def multiply(value_1, value_2):
    multiply = value_1 * value_2
    print(multiply)

def divide(value_1, value_2):
    divide = value_1 / value_2
    print(divide)

def percentage(value_1, value_2):
    percentage = (value_1 / value_2) * 100
    print(percentage)

def power(n,m):
    # n= float(input('Power is n**m, Enter the value of n: '))
    # m= float(input('Power is n**m, Enter the value of m: '))
    power = n**m
    print(power)

if user == 'a':
    add(value_1,value_2)

if user == 's':
    subract(value_1,value_2)

if user == 'm':
    multiply(value_1,value_2)

if user == 'd':
    divide(value_1,value_2)

if user == 'p':
    percentage(value_1,value_2)

if user == 'po':
    power(value_1, value_2)