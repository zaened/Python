#author : Zäned Pasagad
#date : 29. März 2019

tictactoe = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}      #Ankreuzfelder
xFinish = 0
oFinish = 0
guessed = []        #Liste mit ausgefüllten Feldern

def field():        #Feld zeichnen
    print(tictactoe[1]+'|'+tictactoe[2]+'|'+tictactoe[3])
    print(tictactoe[4]+'|'+tictactoe[5]+'|'+tictactoe[6])
    print(tictactoe[7]+'|'+tictactoe[8]+'|'+tictactoe[9])

def horizontal():       #Horizontalabfragen
    global xFinish, oFinish
    if tictactoe[1] == 'X' and tictactoe[4] == 'X' and tictactoe[7] == 'X':
        xFinish = 1
    if tictactoe[2] == 'X' and tictactoe[5] == 'X' and tictactoe[8] == 'X':
        xFinish = 1
    if tictactoe[3] == 'X' and tictactoe[6] == 'X' and tictactoe[9] == 'X':
        xFinish = 1
    if tictactoe[1] == 'O' and tictactoe[4] == 'O' and tictactoe[7] == 'O':
        oFinish = 1
    if tictactoe[2] == 'O' and tictactoe[5] == 'O' and tictactoe[8] == 'O':
        oFinish = 1
    if tictactoe[3] == 'O' and tictactoe[6] == 'O' and tictactoe[9] == 'O':
        oFinish = 1

def vertical():         #Vertikalabfragen
    global xFinish, oFinish
    if tictactoe[1] == 'X' and tictactoe[2] == 'X' and tictactoe[3] == 'X':
        xFinish = 1
    if tictactoe[4] == 'X' and tictactoe[5] == 'X' and tictactoe[6] == 'X':
        xFinish = 1
    if tictactoe[7] == 'X' and tictactoe[8] == 'X' and tictactoe[9] == 'X':
        xFinish = 1
    if tictactoe[1] == 'O' and tictactoe[2] == 'O' and tictactoe[3] == 'O':
        oFinish = 1
    if tictactoe[4] == 'O' and tictactoe[5] == 'O' and tictactoe[6] == 'O':
        oFinish = 1
    if tictactoe[7] == 'O' and tictactoe[8] == 'O' and tictactoe[9] == 'O':
        oFinish = 1

def diagonal():     #Diagonalabfrage
    global xFinish, oFinish
    if tictactoe[1] == 'X' and tictactoe[5] == 'X' and tictactoe[9] == 'X':
        xFinish = 1
    if tictactoe[3] == 'X' and tictactoe[5] == 'X' and tictactoe[7] == 'X':
        xFinish = 1
    if tictactoe[1] == 'O' and tictactoe[5] == 'O' and tictactoe[9] == 'O':
        oFinish = 1
    if tictactoe[3] == 'O' and tictactoe[5] == 'O' and tictactoe[7] == 'O':
        oFinish = 1

def player1():      #Spieler1 = Kreuz + Zeichnung
    tictactoe[choice1] = 'X'
    field()
    guessed.append(choice1)

def player2():      #Spieler2 = Kreuz + Zeichnung
    tictactoe[choice2] = 'O'
    field()
    guessed.append(choice2)

for i in range(0,9):        #Rundencounter
    if i%2 == 0:            #Alle Runden, mit gerader Zahl für Spieler1
        print('Spieler 1 ist dran!\nWähle das Feld, indem du eine Markierung\n(X) setzen willst!')
        field()
        choice1 = int(input())
        if choice1 not in guessed:      #Überschreibschutz für schon ausgefüllte Felder
            player1()
            horizontal()
            vertical()
            diagonal()
            if xFinish == 1:
                break
            if oFinish == 1:
                break
        else:       
            print('Feld schon ausgefüllt!\nWähle erneut!')
            choice1 = int(input())
            player1()
            horizontal()
            vertical()
            diagonal()
            if xFinish == 1:
                break
            if oFinish == 1:
                break
    if i%2 == 1:        #Alle Runden mit ungerader Zahl für Spieler2
        print('Spieler 2 ist dran!\nWähle das Feld, indem du eine Markierung\n(O) setzen willst!')
        choice2 = int(input())
        if choice2 not in guessed:      #Überschreibschutz für schon ausgefüllte Felder
            player2()
            horizontal()
            vertical()
            diagonal()
            if xFinish == 1:
                break
            if oFinish == 1:
                break
        else:       
            print('Feld schon ausgefüllt!\nWähle erneut!')
            choice2 = int(input())
            player2()
            horizontal()
            vertical()
            diagonal()
            if xFinish == 1:
                break
            if oFinish == 1:
                break

if xFinish == 1:        #Gewinner/Verlierernachricht
    print('Spieler 1 hat gewonnen!')
elif oFinish == 1:
    print('Spieler 2 hat gewonnen!')
elif xFinish == 0 and oFinish == 0:
    print('Diese Partie endet in einem Unentschieden!')
        
