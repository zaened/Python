# author : Zäned Pasagad
# date : 20.04.2021

import datetime

birthDates = []     # Liste aller Geburtstage
moreData = ''       # Abbruchvariable

def entry():
    global birthDates
    x = int(input('Jahr : '))
    y = int(input('Monat : '))
    z = int(input('Tag : '))
    bDay = datetime.datetime(x,y,z)
    birthDates.append(bDay)

print(' Geburtstagssortierung '.center(80,'='))

while moreData == '':
    entry()
    moreData = input('Möchten sie mehr Daten eingeben? Enter -> Ja, N -> Nein ').upper()

birthDates.sort()

for i in range(0,len(birthDates)):
    birthDates[i] = birthDates[i].strftime('%x')

print('\n'.join(birthDates))
input(' Ende '.center(80,'='))
