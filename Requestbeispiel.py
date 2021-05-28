# author : Zäned Pasagad
# date : 27.05.2021

import requests, pyperclip, os

input('Kopieren sie eine URL, bevor sie fortfahren!')
url = pyperclip.paste()
name = input('Gib den Namen der Datei an: ')

# Response - Objekt erzeugen, mit der URL
response = requests.get(url)



# Überprüfen des Downloaderfolgs
if response.raise_for_status() == None:
    try:
        with open(name, 'wb') as file:
            for character in response.iter_content():
                file.write(character)
    except (HTTPError, MissingSchema):
        print('Verarbeitung nicht möglich!\nGib eine funktionierende Webseite an oder versuche es später!\nWebseite: ')
    
input('Ihre Webseite wurde unter ' + os.getcwd() + ' abgespeichert!')
