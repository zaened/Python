# author : Zäned Pasagad
# date : 03.08.2021

import random
import tkinter

# Variablen
player1 = 0
player2 = 0

stone = 1
scissor = 2
paper = 3

# Spiellogik
def resCalc():
    '''Funktion zur Ergebnisermittlung'''
    if player2 == stone:
        text.insert(tkinter.END, 'Spieler 2 wählte Stein!\n')
    elif player2 == scissor:
        text.insert(tkinter.END, 'Spieler 2 wählte Schere!\n')
    else:
        text.insert(tkinter.END, 'Spieler 2 wählte Papier!\n')
    result = player1 - player2
    if result == -1 or result == 2:
        text.insert(tkinter.END, 'Spieler 1 gewinnt!')
    elif result == 1 or result == -2:
        text.insert(tkinter.END, 'Spieler 2 gewinnt!')
    else:
        text.insert(tkinter.END, 'Unentschieden!')

def chooseStone():
    '''Wählt Stein - für Anknüpfung an Button + Löschen des vorherigen Textboxinhalts'''
    global player1, player2
    text.delete('1.0', 'end')
    player1 = stone
    player2 = random.randint(1,3)
    resCalc()

def chooseScissor():
    '''Wählt Schere - für Anknüpfung an Button + Löschen des vorherigen Textboxinhalts'''
    global player1, player2
    text.delete('1.0', 'end')
    player1 = scissor
    player2 = random.randint(1,3)
    resCalc()

def choosePaper():
    '''Wählt Papier - für Anknüpfung an Button + Löschen des vorherigen Textboxinhalts'''
    global player1, player2
    text.delete('1.0', 'end')
    player1 = paper
    player2 = random.randint(1,3)
    resCalc()

# GUI
window = tkinter.Tk()
window.geometry('750x500')
window.title('Schere, Stein, Papier')

# Frames
frame1 = tkinter.Frame(window)
frame1.pack(side=tkinter.TOP)
frame2 = tkinter.Frame(window)
frame2.pack(side=tkinter.BOTTOM)

# Textbox
text = tkinter.Text(frame1)
text.pack()
text.insert(tkinter.END, 'Spiele Schere, Stein, Papier!')

# Buttons
button1 = tkinter.Button(frame2, text='Schere', command=chooseScissor)
button1.pack(side=tkinter.LEFT)
button2 = tkinter.Button(frame2, text='Stein', command=chooseStone)
button2.pack(side=tkinter.LEFT)
button3 = tkinter.Button(frame2, text='Papier', command=choosePaper)
button3.pack(side=tkinter.RIGHT)

window.mainloop()
