# autor : Zäned Pasagad
# date : 26.05.2021

import PyPDF2

filepath = r'' + input('Bitte geben sie einen Dateipfad ein: ')
# PDF-Dateien werden wie Txt-Dateien mit open() geöffnet
with open(filepath, 'rb') as pdfFile:
    # PyPDF2 erstellt ein PDFfilereader - Objekt
    reader = PyPDF2.PdfFileReader(pdfFile)
    # Es wird die Seite rausgepickt, die gelesen werden soll
    page = reader.getPage(0)
    # Jetzt wird der Text extrahiert und ausgegeben
    print(page.extractText())
    input('Ende'.center(40, '='))
