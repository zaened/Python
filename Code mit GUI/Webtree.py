# author : Zäned Pasagad
# date : 09.06.2021

import tkinter, webbrowser

# Funktionen
def openYoutube():
    webbrowser.open('https://www.youtube.com')
    
def openGithub():
    webbrowser.open('https://www.github.com')

def openLinkedIn():
    webbrowser.open('https://www.linkedin.com')

def openInstagram():
    webbrowser.open('https://www.instagram.com')

def openTwitter():
    webbrowser.open('https://www.twitter.com')

def openStackoverflow():
    webbrowser.open('https://www.stackoverflow.com')
    
# Fenster initialisieren
root = tkinter.Tk()
root.title('Webbuttons')
root.geometry('300x400')
root.minsize(width=300, height=400)
root.maxsize(width=300, height=400)
root.configure(bg='black')

# Frames
frame1 = tkinter.Frame(root)
frame1.pack(side=tkinter.LEFT)
frame2 = tkinter.Frame(root)
frame2.pack(side=tkinter.RIGHT)
frame3 = tkinter.Frame(root)
frame3.pack(side=tkinter.TOP)
frame4 = tkinter.Frame(root)
frame4.pack(side=tkinter.BOTTOM)

# Buttons
button1 = tkinter.Button(frame1, text='Youtube', width=16, bg='red', command=openYoutube)
button1.pack(side=tkinter.TOP)
button2 = tkinter.Button(frame1, text='Github', width=16, bg='slate grey', command=openGithub)
button2.pack()
button3 = tkinter.Button(frame1, text='LinkedIn',width=16, bg='blue', command=openLinkedIn)
button3.pack()
button4 = tkinter.Button(frame2, text='Instagram', width=16, bg='pink', command=openInstagram)
button4.pack(side=tkinter.TOP)
button5 = tkinter.Button(frame2, text='Twitter', width=16, bg='sky blue', command=openTwitter)
button5.pack()
button6 = tkinter.Button(frame2, text='Stackoverflow', width=16, bg='orange', command=openStackoverflow)
button6.pack()
button7 = tkinter.Button(frame4, text='Close', width=10, command=root.destroy)
button7.pack()

# Label
label = tkinter.Label(frame3, text='Social Media', fg='white', bg='black')
label.pack()

root.mainloop()
