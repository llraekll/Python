import random


def rps():
    me = str(input('Rock, paper, sissors....Shoot: '))
    pc = random.choice(['rock', 'paper', 'sissors'])

    if me == pc:
        print(pc)
        print( "tie nigga!")
    elif analize(me, pc):
        print(pc)
        print('You won this nigga!')
    else:
        print(pc)
        print('I won this nigga!')


def analize(w, l):
    if (w =='rock' and l =='sissors') or (w =='sissors' and l =='paper') or (w =='paper' and l =='rock'):
        return True


rps()