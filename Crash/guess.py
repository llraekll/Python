import random
from logics import compare


def guess():
    m = random.randint(1,10)
    n = 0
    while n != m:
        n = int(input('Enter number nigga:'))
        if n > m:
            print('Too high nigga')
        elif n < m:
            print('Too low nigga')
        else:
            print('You right nigga, da numba is', m)



if __name__ == '__main__':
    guess()