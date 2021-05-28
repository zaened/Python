# author : Zäned Pasagad
# date : 03.05.2021

# Start
print(' Mad - Libs - Generator '.center(80, '='))

# Variablen mit input
year = input('Bitte Jahreszahl eingeben : ')
trooper = input('Bitte Truppenname eingeben : ')
city = input('Bitte Stadtnamen eingeben : ')
heroes = input('Bitte Namen für Heldengruppe eingeben : ')
villains = input('Bitte Namen für Bösewichtgruppe eingeben : ')

# Lückentext mit Variablen füllen
print(''.center(80, '='))
text = '''Im Jahre %s fielen die %s in unsere Heimatstadt %s ein!
Um unsere Heimatstadt zu schützen, sandte der Bürgermeister die Stadtwacht, welche unter dem Namen %s bekannt war aus, um uns vor der Gefahr, die von den %s
ausging zu verteidigen...vergebens! Kurz darauf traten unsere Retter, die %s in Erscheinung, welche uns vor den %s beschützte, indem sie in der Schlacht des
Jahrhunderts jedes Mitglied der %s in einem Duell besiegte!''' %(year, villains, city, trooper, villains, heroes, villains, villains)

# Text ausgeben
print(text)
input(' Ende '.center(80, '='))
