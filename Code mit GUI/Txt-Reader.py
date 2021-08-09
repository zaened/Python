# author : Zäned Pasagad
# date : 01.08.2021

import tkinter
from tkinter.filedialog import askopenfile

def reading():
    '''Dient zum Einlesen der Txt-Dateien. Wird an einen Button geknüpft.'''
    file = askopenfile(mode = 'r', filetypes = [('Textdateien', '*.txt')])
    if file is not None:
        textbox.delete('1.0', 'end')
        textbox.insert(tkinter.END, file.read())

# Fenster
root = tkinter.Tk()
root.geometry('800x600')
root.title('Txt-Reader')

# Frames
frame1 = tkinter.Frame(root)
frame1.pack(side=tkinter.BOTTOM)
frame2 = tkinter.Frame(root)
frame2.pack(side=tkinter.TOP)

# Buttons
button1 = tkinter.Button(frame1, text='Datei wählen', command=reading)
button1.pack(side=tkinter.LEFT)
button2 = tkinter.Button(frame1, text='Schließen', command=root.destroy)
button2.pack(side=tkinter.RIGHT)

# Textfeld
textbox = tkinter.Text(frame2, height=20, width=70)
textbox.insert(tkinter.END, 'Willkommen bei dem Txt - Reader von Zäned Pasagad!')
textbox.pack()

root.mainloop()
