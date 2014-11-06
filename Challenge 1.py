"""
1. Create a program that prints a list of words in random order. The program should
   print all the words and not repeat any.
"""
#Challenge 1
#Andrew Hecky
#11/6/2014


import random
WORDS =['acorn', 'argue', 'belive', 'blank', 'blaze', 'boat', 'bounded', 'brale', 'brush', 'bypass', 'camper', 'chewy', 'complete', 'cream', 'cubicle', 'cyrus', 'dashing',
        'dion','diving', 'donor', 'dream', 'exert', 'father', 'fellow', 'finland', 'gnaw', 'grass', 'guild', 'gush', 'gusher', 'happy', 'herp', 'inn', 'joyride', 'lead',
        'lonely', 'lower', 'minimum', 'mother', 'mugger', 'never', 'nissan', 'nonsense', 'organ', 'organic', 'perfect', 'poked', 'raise', 'read', 'reded', 'refuge', 'scruff',
        'scrumpy', 'seed', 'sherman','similar', 'soviet','spawn','spawner', 'sponsor', 'surer', 'sweater', 'topmost', 'total', 'tutted', 'vehicle', 'winch']

AvaWords = WORDS

random.shuffle(AvaWords)

print('Word List: ')
for i in AvaWords :
    print('\t'+i[0].upper() + i[1:])


