# author: Zäned Pasagad
# date: 10.September 2020

import random

words = ['TEST','ELEKTRONIK','KOPFHÖRER','STROM','COMPILER','DISPLAY','PROGRAMM','UNI','ROBOTER','CODE']
l = len(words) - 1      # Länge der Liste words
b = ''      # Zufälliges Wort
c = ''      # Vergleichsvariable und Ersatz
d = []      # Liste an bereits vermuteten Buchstaben (egal ob richtig oder falsch)
e = 0       # Counter
f = 0       # Länge des Wortes

def choice():
    global b,c,f
    b = words[random.randint(0,l)]  # Zufallswortwahl
    c = list(len(b) * '_')      # Erstellung der Anonymisierung des gesuchten Wortes
    f = len(b)      # Länge des gesuchten Wortes
    print('Das gesuchte Wort lautet:'+str(c))
    print('Raten sie einen Buchstaben!')
    
def draw():     # Zeichnen des Galgenmännchens
    if e == 1:
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('________')
    elif e == 2:
        print('')
        print('   |')
        print('   |')
        print('   |')
        print('   |')
        print('   |')
        print('   |')
        print('___|____')
    elif e == 3:
        print('  ___________')
        print('   |')
        print('   |')
        print('   |')
        print('   |')
        print('   |')
        print('   |')
        print('___|____')
    elif e == 4:
        print('   ___________')
        print('   |         |')
        print('   |         |')
        print('   |')
        print('   |')
        print('   |')
        print('   |')
        print('___|____')
    elif e == 5:
        print('   ___________')
        print('   |         |')
        print('   |         |')
        print('   |         O')
        print('   |')
        print('   |')
        print('   |')
        print('___|____')
    elif e == 6:
        print('   ___________')
        print('   |         |')
        print('   |         |')
        print('   |         O')
        print('   |         |')
        print('   |')
        print('   |')
        print('___|____')
    elif e == 7:
        print('   ___________')
        print('   |         |')
        print('   |         |')
        print('   |         O')
        print('   |         |')
        print('   |        / \ ')
        print('   |')
        print('___|____')
    elif e == 8:
        print('   ___________')
        print('   |         |')
        print('   |         |')
        print('   |         O')
        print('   |        \|/')
        print('   |        / \ ')
        print('   |')
        print('___|____')

def swap(search):       # Funktion zum Tausch von unbekannten Zeichen in erratene, richtige Zeichen
    global b,c,e
    search = search.upper()
    if search not in d:     # Falls Buchstabe nicht schon erraten
        if search in b:     # Falls Buchstabe in Wort
            for i in range(0,f,1):      # Durchlaufen des Wortes, um Buchstabe an der richtigen Stelle ersetzen zu können
                if search == b[i]:      # Falls Buchstabe an der Stelle i des Wortes
                    c[i] = search       # Ersetze Unterstrich durch erratenen Buchstaben an Stelle i
            print('Richtig geraten! Weiter so!')
            print('Gesuchtes Wort'+str(c))
        else:
            print('Leider haben sie falsch geraten! Versuchen sie es nochmal!')
            print('Gesuchtes Wort:'+str(c))
            e += 1
    else:
        print('Dieser Buchstabe wurde schon erraten! Versuchen sie es nochmal!')
        print('Gesuchtes Wort:'+str(c))
        e += 1
    d.append(search)

print('Herzlich Willkommen! Sie spielen das Spiel : Galgenmännchen!')
print('Regel: Alle Eingaben müssen in Buchstaben erfolgen und sie können nur ein Buchstaben nach dem anderen erraten!')
print('Das Spiel wird solange fortgesetzt, bis das Galgenmännchen gezeichnet wurde.')
choice()

while e < 8:
    swap(input())
    draw()
    if e == 8 or '_' not in c:      # Falls Versuche aufgebraucht sind oder alle Buchstaben korrekt erraten sind, brich Schleife ab
        break

if e == 8:      # Falls Versuche aufgebraucht -> Verloren
    print('Sie haben verloren! Das gesuchte Wort lautet: '+b)
    input()

if '_' not in c:        # Falls Wort erraten -> Gewonnen
    print('Sie haben gewonnen! Das gesuchte Wort lautet: '+b)
    input()
