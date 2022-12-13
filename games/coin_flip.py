import random

i = str(input('Press enter for a coin flip'))
options = ['Thumbs up!', 'Thumps down!']
choice = random.choice(options)
count = 0 
while count < 2000:
    print('|Flipping                                                                |')
    print('|                                                                        |')
    print('|                                                                        |')
    print('|                                Flipping                                |')
    print('|                                                                        |')
    print('|                                                                        |')
    print('|                                                                Flipping|')
    count +=1
else:
    print(choice)