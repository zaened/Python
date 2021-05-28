# author :  Zäned Pasagad
# date : 15.05.2021

name = input('Geben sie den Dateipfad oder Dateinamen an: ')
file = open(r'' + name)
print(file.read())
input(' Ende '.center(40, '='))
file.close()
