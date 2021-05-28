# author : Zäned Pasagad
# date : 08.05.2021

# to do: Eingabe des gesuchten Jahres
searched = int(input('Bitte geben sie das gesuchte Jahr ein : '))
leapYear = 1972
switchGuard = 0

if searched < leapYear:
    switchGuard = -1
elif searched > leapYear:
    switchGuard = 1
elif searched == leapYear:
    input('Das Jahr ' + str(searched) + ' ist ein Schaltjahr!')
    quit()
    
while switchGuard == 1:
    if searched > leapYear:
        leapYear += 4
    elif searched < leapYear:
        break
    if searched == leapYear:
        input('Das Jahr ' + str(searched) + ' ist ein Schaltjahr!')
        quit()

while switchGuard == -1:
    if searched < leapYear:
        leapYear -= 4
    elif searched > leapYear:
        break
    if searched == leapYear:
        input('Das Jahr ' + str(searched) + ' ist ein Schaltjahr!')
        quit()

input('Das Jahr ' + str(searched) + ' ist kein Schaltjahr!')
