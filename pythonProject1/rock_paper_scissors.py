import random
mychoice=int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.'))
machinechoice = random.randint(0,2)
print(machinechoice)
if mychoice==0 and machinechoice==2:
    print('You win')
elif    mychoice==2 and machinechoice==0:
    print('You lose')
elif mychoice<machinechoice:
    print('You lose')
elif mychoice==machinechoice:
    print('Draw')
else:
    print('You win')