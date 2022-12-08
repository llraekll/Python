import random

def guess(x):
    low = 1
    high = x
    feedback = 1
    while feedback != 'c':
        if low == high:
            print(f'{low} is the chosen numba')
            break
        else:
            guess = random.randint(low, high)
            print(guess)
            print(f'h for high, l for low, c for correct nigga!')
            feedback = str(input('Enter the options nigga!: '))
            if feedback == 'h':
                high = guess -1 
            elif feedback == 'l':
                low = guess +1
    print(f'PC guessed it nigga!, the numba is {guess}')


guess(10)