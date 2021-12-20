import tkinter
import smtplib

# Author : Zäned
# Date : 13.11.2021

def mailWindow():
    '''Erstelle E - Mail - Fenster.'''
    global empfaengerentry, betreffentry, textfeld, window2
    window2 = tkinter.Toplevel(window)
    window2.geometry('500x500')
    window2.minsize(500, 500)

    empfaenger = tkinter.StringVar()
    empfaengerentry = tkinter.Entry(window2, textvariable=empfaenger)
    empfaenger.set('E-Mail')
    empfaengerentry.pack()
    
    betreff = tkinter.StringVar()
    betreffentry = tkinter.Entry(window2, textvariable=betreff)
    betreff.set('Betreff')
    betreffentry.pack()

    textfeld = tkinter.Text(window2)
    textfeld.pack()

    sendmailbutton = tkinter.Button(window2, text='Senden', command=sending)
    sendmailbutton.pack()

    logoutbutton = tkinter.Button(window2, text='Ausloggen', command=logout)
    logoutbutton.pack()
    
    window2.mainloop()
    
def checkLogin():
    '''Check Login - Daten und Verbindungsaufbau.'''
    global connection, email_submit
    email_submit = email.get()
    password_submit = password.get()
    connection = smtplib.SMTP('smtp.office365.com', 587)
    connection.ehlo()
    connection.starttls()
    connection.login(email_submit, password_submit)
    mailWindow()

def sending():
    get_empfaenger = empfaengerentry.get()
    get_betreff = betreffentry.get()
    get_email_text = textfeld.get('1.0', 'end')
    #print(email_submit + get_empfaenger + 'Subject:' + get_betreff + '\n\n' + get_email_text)
    connection.sendmail(email_submit, get_empfaenger, 'Subject:' + get_betreff + '\n\n' + get_email_text)

def logout():
    connection.quit()
    window.destroy()

window = tkinter.Tk()
window.geometry('300x100')
window.minsize(300, 100)
window.title('Z-Programm')

# Login - Felder

# E - Mail - Feld
text1 = tkinter.StringVar()
email = tkinter.Entry(window, textvariable=text1, width=30)
text1.set('E-Mail')
email.pack()

# Passwortfeld
text2 = tkinter.StringVar()
password = tkinter.Entry(window, textvariable=text2, show='*', width=30)
text2.set('Passwort')
password.pack()

# Login - Button
loginbutton = tkinter.Button(window, text='Einloggen', command=checkLogin)
loginbutton.pack(side=tkinter.BOTTOM)

window.mainloop()
