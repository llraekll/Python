def primes():
    n = int(input('Start numba: '))
    m= int(input('End numba: '))
    print(f'Primes between {n} and {m} are:')

    for num in range(n,m):
        if num >1:
            for i in range(2,num):
                if (num%i) == 0:
                    break
            else:
                print(num)



if __name__ == '__main__':
    primes()