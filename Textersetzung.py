# author : Zäned Pasagad
# date : 21.04.2021

text = ''''''       # Abspeicherung des Textes

print(' Textersetzung '.center(40,'='))

text = input('Geben sie Ihren Text ein : ')
newText = text.replace(input('Zu ersetzendes Wort : '),input('Ersatzwort : '))
print(newText)

input(' Ende '.center(40,'='))

