# author : Zäned Pasagad
# date : 03.05.2021

import random

# Schwierigkeitsgrad erstellen (Menge vergrößern)
easy = 50
medium = 100
hard = 1000
trolling = 1000000

chosenDifficulty = input('Bitte wählen sie eine Schwierigkeitsstufe aus : [Einfach, Mittel, Schwer]').upper()

i = 0
turns = 1

if chosenDifficulty == 'EINFACH':
    i = easy
    turns += 20
elif chosenDifficulty == 'MITTEL':
    i = medium
    turns += 15
elif chosenDifficulty == 'SCHWER':
    i = hard
    turns += 10
elif chosenDifficulty != 'EINFACH' or chosenDifficulty != 'MITTEL' or chosenDifficulty != 'SCHWER':
    i = trolling
    turns += 5

# Zufallszahl erstellen
number = random.randint(1, i)

# Abfrage der Nummer
for turnCount in range(1,turns):
    print('Wählen sie eine Zahl zwischen 1 und ' + str(i))
    choice = int(input('Zahl : '))

    # Abbruchbedingung + Tipps
    if choice > number:
        print('Versuchen sie es nochmal! Die gesuchte Zahl ist kleiner als ' + str(choice) + '.\nSie haben noch ' + str(
            turns - turnCount - 1) + ' Versuche!')
    elif choice < number:
        print('Versuchen sie es nochmal! Die gesuchte Zahl ist größer als ' + str(choice) + '.\nSie haben noch ' + str(
            turns - turnCount - 1) + ' Versuche!')
    elif choice == number:
        break

# Gewinner/Verlierernachricht
if turnCount != turns - 1:      # Das - 1 dient zum korrekten Bewerten der Gewinnbedingung (for - Schleife geht bis 20)
    print('Herzlichen Glückwunsch! Die gesuchte Zahl ist tatsächlich die : ' + str(number) + '.')
    input(' GEWONNEN '.center(80, '='))
else:
    print('Sie haben verloren! Die gesuchte Zahl lautet : ' + str(number) + '.')
    input(' VERLOREN '.center(80, '='))
