import random


def guess():
    m = random.randint(1, 20)
    n = 0
    while n != m:
        n = int(input('Numba nigga: '))
        if n < m:
            print('Too low nigga')
        elif n > m:
            print('Too high nigga')
        else:
            print(f'You got it nigga, {m} is da numba')
    print('Thanks fa playin nigga')


if __name__ == '__main__':
    guess()
