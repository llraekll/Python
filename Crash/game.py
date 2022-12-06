import random
from logics import compare

def game():
    random_number = random.randint(1,100)
    result = ''
    while result != 'You right nigga':
        number = int(input('Enter a number nigga:'))
        result= compare(number,random_number)
        print(result)

if __name__ == '__main__':
    game()