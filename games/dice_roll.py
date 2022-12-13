import random

dice_roll = str(input('Enter R for rolling the dice ')).upper()
number = random.randint(1,6)
# number = 1 
while dice_roll == 'R':
    if number == 1:
        count = 0 
        while count < 1000:
            print('|Roll    |')
            print('|  Roll  |')
            print('|    Roll|')
            count +=1
        else:
            print('        ')
            print('|        |')
            print('|   R1   |')
            print('|        |')
            break
        
    if number == 2:
        count = 0 
        while count < 1000:
            print('|Roll    |')
            print('|  Roll  |')
            print('|    Roll|')
            count +=1
        else:
            print('        ')
            print('|R2      |')
            print('|        |')
            print('|      R2|')
            break
    if number == 3:
        count = 0 
        while count < 1000:
            print('|Roll    |')
            print('|  Roll  |')
            print('|    Roll|')
            count +=1
        else:
            print('        ')
            print('|R3      |')
            print('|   R3   |')
            print('|      R3|')
            break
    if number == 4:
        count = 0 
        while count < 1000:
            print('|Roll    |')
            print('|  Roll  |')
            print('|    Roll|')
            count +=1
        else:
            print('        ')
            print('|R4    R4|')
            print('|        |')
            print('|R4    R4|')
            break
    if number == 5:
        count = 0 
        while count < 1000:
            print('|Roll    |')
            print('|  Roll  |')
            print('|    Roll|')
            count +=1
        else:
            print('        ')
            print('|R5    R5|')
            print('|   R5   |')
            print('|R5    R5|')
            break
    if number == 6:
        count = 0 
        while count < 1000:
            print('|Roll    |')
            print('|  Roll  |')
            print('|    Roll|')
            count +=1
        else:
            print('        ')
            print('|R6    R6|')
            print('|R6    R6|')
            print('|R6    R6|')
            break

    # dice_roll = str(input('Enter R for rolling the dice again ')).upper()