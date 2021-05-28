# author : Zäned Pasagad
# date : 27.05.2021

import pyperclip

name = input() + '.txt'

with open(name, 'w') as file:
    file.write(pyperclip.paste())
