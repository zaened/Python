# author: Zäned Pasagad
# date: 02.07.2020

antwort1 = 0
ergebnis1 = 0

def Antwort():      # Wird zum Berechnen des Ergebnisses gebraucht
    global antwort1,ergebnis1
    if antwort1 == 'A':
        ergebnis1 = ergebnis1 + 1
    elif antwort1 == 'B':
        ergebnis1 = ergebnis1 + 2
    elif antwort1 == 'C':
        ergebnis1 = ergebnis1 + 3
    elif antwort1 == 'D':
        ergebnis1 = ergebnis1 + 4
    elif antwort1 == 'E':
        ergebnis1 = ergebnis1 + 5

def Auswertung():       # Nachdem alle Fragen beantwortet wurden, wird je nach Wert von Ergebnis1 ein anderes Ergebnis angezeigt
    if ergebnis1 >= 10 and ergebnis1 <= 18:
        print('Du bist ein Magier! Du nutzt dein Wissen über arkane Mächte und Zauber ein, um deine Gegner zu pulverisieren. Intelligent und schnelldenkend löst du mit deinem Wissen Probleme!')
        input()
    elif ergebnis1 >= 19 and ergebnis1 <= 27:
        print('Du bist ein Jäger! Du nutzt Pfeil und Bogen, als auch deine Umgebung geschickt zu deinem Vorteil! Fokussiert visierst du dein Ziel aus der Ferne an und verpasst ihm mit einem Schuss einen Tritt ins Jenseits!')
        input()
    elif ergebnis1 >= 28 and ergebnis1 <= 36:
        print('Du bist ein Assassine! Du gehst mit atemberaubender Geschwindigkeit auf dein Ziel los, tötest es und ziehst dich dann zurück. Du bist geschickt, opportunistisch und berechnend!')
        input()
    elif ergebnis1 >= 37 and ergebnis1 <= 45:
        print('Du bist ein Krieger! Du gehst furchtlos mit deinem Schild und Schwert oder mit schwerer Rüstung in den Kampf und bist meist ein Anführer!')
        input()
    elif ergebnis1 >= 46 and ergebnis1 <= 50:
        print('Du bist ein Priester! Du heilst deine Verbündeten, was meist eine ziemlich undankbare Aufgabe ist, dennoch bist du derjenige, welcher über Erfolg oder Niederlage in Raids entscheiden kann!')
        input()

for i in range(0,10,1):     # Fragen für den Test
    if i == 0:
        print('Was findest du am coolsten?')
        print('A : Gegner mit mächtigen Zaubern umhauen.')
        print('B : Aus sicherer Entfernung mit Pfeilen den Gegnern das Leben schwer machen.')
        print('C : Den Gegner aus dem Schatten überraschen, ihn töten und dann zum Rückzug antreten.')
        print('D : Mutig in den Kampf ziehen und dabei die Gegner mit dem Schwert töten.')
        print('E : Meine Kameraden mit Heilfähigkeiten am Leben halten.')
        antwort1 = input().upper()
        Antwort()
    elif i == 1:
        print('Welche Waffe würdest du im Kampf nutzen?')
        print('A : Stab/Zepter')
        print('B : Pfeil und Bogen/Armbrust')
        print('C : Dolche,Wurfmesser und Rauchbomben')
        print('D : Langschwert(und Schild)')
        print('E : Gar keine, ich heile nur!')
        antwort1 = input().upper()
        Antwort()
    elif i == 2:
        print('Welche Stats sind dir wichtig?')
        print('A : Intelligenz')
        print('B : Fokus/Kraft')
        print('C : Geschicklichkeit/Geschwindigkeit')
        print('D : Kraft/Zähigkeit')
        print('E : Zähigkeit/Intelligenz')
        antwort1 = input().upper()
        Antwort()
    elif i == 3:
        print('Welche Kleidung bevorzugst du?')
        print('A : Roben')
        print('B : Lederrüstung/Tarnfarbende Kleidung')
        print('C : Dunkle Kleidung/Mäntel')
        print('D : Schwere Rüstung aus Silber oder Gold')
        print('E : Priesterumhang')
        antwort1 = input().upper
        Antwort()
    elif i == 4:
        print('Wähle eine Charaktereigenschaft!')
        print('A : Intelligent/Buchgelehrt')
        print('B : Ruhig/Naturliebend')
        print('C : Opportunistisch/Geduldig')
        print('D : Mutig/Anführend')
        print('E : Hilfsbereit/Friedliebend')
        antwort1 = input().upper()
        Antwort()
    elif i == 5:
        print('Lieblingsrolle in League')
        print('A : Mid/Supp')
        print('B : ADC/Jungle')
        print('C : Mid/Top/Jungle')
        print('D : Top/Jungle')
        print('E : Supp/Jungle')
        antwort1 = input().upper()
        Antwort()
    elif i == 6:
        print('Lebensphilosophie?')
        print('A : Wissen ist Macht!')
        print('B : Jedem des seine!')
        print('C : Eins nach dem Anderen!')
        print('D : Nicht reden, sondern machen!')
        print('E : Was du nicht willst was man dir tu, dass füg auch keinem anderem zu!')
        antwort1 = input().upper()
        Antwort()
    elif i == 7:
        print('Lieblingsort?')
        print('A : Bibliothek')
        print('B : Die Natur')
        print('C : Eine Großstadt')
        print('D : Ein Palast oder das Schlachtfeld')
        print('E : Kirche oder jeder Ort an dem meine Familie ist')
        antwort1 = input().upper()
        Antwort()
    elif i == 8:
        print('Was ist einer deiner Schwächen?')
        print('A : Bin nicht sehr gut mit den Händen.')
        print('B : Vermeide Risiken.')
        print('C : Bin ein Einzelgänger.')
        print('D : Ich bin stur.')
        print('E : Ich habe manchmal keine eigene Meinung.')
        antwort1 = input().upper()
        Antwort()
    elif i == 9:
        print('Welche Fähigkeit spricht dich an?')
        print('A : Die Erschaffung eines Portals mit dem ich und meine Freunde überall hin können!')
        print('B : Die Fähigkeit, meine Ziele ab einem Radius von 5KM zu sichten!')
        print('C : Unsichtbarkeit und Kurzstreckenteleportation (wenige Meter)!')
        print('D : Meine Haut mit Titan stählen!')
        print('E : Meine Kameraden global heilen!')
        antwort1 = input().upper()
        Antwort()
        Auswertung()