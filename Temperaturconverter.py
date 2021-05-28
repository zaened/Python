# author : Zäned Pasagad
# date : 20.05.2021

def cInF(temp):
    '''Rechnet von °C in °F um.'''
    tempF = (int(temp) * 9/5) + 32
    return tempF

def fInC(temp):
    '''Rechnet von °F in °C um.'''
    tempC = (int(temp) - 32) * 5/9
    return tempC

loop = True

# Hauptprogramm
while loop:

    # Wählen der Einheitsumrechnung
    convertChoice = input('''Welche Einheit möchten sie umrechnen?
Von °C in °F (1) oder von °F in °C (2)? ''')

    if convertChoice == '1':
        print(cInF(input('Tragen sie die Temperatur in °C ein: ')))
    elif convertChoice == '2':
        print(fInC(input('Tragen sie die Temperatur in °F ein: ')))

    setLoop = input('Möchten sie weitere Umrechnungen vornehmen? Ja oder Nein (N)? ').upper()
    if setLoop == 'N':
        loop = False
