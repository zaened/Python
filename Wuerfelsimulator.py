# author : Zäned Pasagad
# date : 04.05.2021

import random
diceThrow = 'y'

print(' Würfelsimulator '.center(80, '='))

# Würfelzahl generieren
while diceThrow == 'y':
    print(random.randint(1, 6))

    # Abbruchbedingung
    diceThrow = input('Möchten sie nochmal werfen? (y) -> Ja, (n) -> Nein ')
