# author : Zäned Pasagad
# date : 09.05.2021

searched = int(input('Bitte geben sie das gesuchte Jahr ein : '))

if searched % 4 == 0:
    print('Das Jahr ' + str(searched) + ' ist ein Schaltjahr!')
else:
    print('Das Jahr ' + str(searched) + ' ist kein Schaltjahr!')

input()
