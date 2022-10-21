# Aufgabe: Wörter raten
# 
# Schreiben Sie ein kleines Spiel bei dem man Wörter erraten muss.
# Vorgabe: eine Liste mit Tiergattungen, mindestens 21 Wörter
#          Für das Spiel mit dem User: 
#               - ein Wort zufällig auswählen 
#               - user gibt einen Buchstaben ein oder "ende"
#               - Bei "ende" Eingabe: das Spiel beenden
#               - Bei Buchstabeneingabe
#                   - Buchstabe ist im Wort enthalten: das Wort mit dem Format
#                       ...X...X.. den Buchstaben am jeweiligen Platz ausgeben
#                       sind vorher schon Buchstaben richtig gewesen, diese ebenfalls 
#                       mit ausgeben:..aX..Xen
#                       sind alle Buchstaben erkannt: Lob ausgeben
#               - Maximale Anzahl an Versuchen: Wortlänge + 9
#           Zeit: 20220427 13:40 Uhr - 15:45 Uhr -- Viel Erfolg und Spaß!


import random

tierListe = ["affe", "delphin", "hund", "katze", "maus", "fledermaus", "büffel", "tiger", "panther", "igel", "vogel", "wal" , "hai", "hirsch", "huhn", "nilpferd", "nashorn", "biene", "spinne", "pferd","löwe"]

tier = tierListe[random.randrange(len(tierListe)-1)]


versuche = 9 
erRaten = ""

#print("Zum Starten go eingeben zum Beenden quit eingeben")
#start = input("Befehl eingeben: ")
#if start == "start":
#    while start = "start" or "quit" 
#elif start == "quit":
#    print("Beendet")
#   quit()
#else:
#    print("Befehl nicht erkannt")
#    start = input("Befehl eingeben: ")

print("Das Spiel startet")
print("________________________________________________________")
while (versuche != 0):
    raten = input("Bitte gebe nur einen Buchstaben ein: ")
    
    while not raten.isalpha() or len(raten) >1:
        if  raten == "ende":
            exit()
        elif raten == tier:
            print("Gewonnen")
            exit()
        elif not raten.isalpha():
            print("Bitte nur Buchstaben eingeben")
        elif len(raten) >1:
            print("Bitte nur einen einzelnen Buchstaben")
        raten = input("Bitte gib nur einen Buchstaben ein: ")      
    
    erRaten = erRaten + raten.lower()
    gewonnen = True      
    versuche8 = ('''
                
                | 
                |
                |
                |
            ____|_____''')
    versuche7 = ('''
                
                __________
                |
                |
                |
                |
            ____|_____''')

    versuche6 = ('''
                
                __________
                |        |
                |        o
                |
                |
            ____|_____''')

    versuche5 = ('''
                
                __________
                |        |
                |        o
                |        |
                |
            ____|_____''')

    versuche4 =  ('''
                
                __________
                |        |
                |        o
                |       /|
                |
            ____|_____''')

    versuche3 = ('''
                
                __________
                |        |
                |        o
                |       /|\\
                |
            ____|_____''')
    versuche2 = ('''
                
                __________
                |        |
                |        o
                |       /|\\
                |       /
            ____|_____''')
    versuche1 = ('''
                
                __________
                |        |
                |        o
                |       /|\\
                |       / \\ 
            ____|_____''')

    versuche0 = ('''
                
                __________
                |        |
                |        o
                |       /|\\     HANGman dead
                |       / \\
            ____|_____''')


    if raten not in tier:
        versuche = versuche -1
        print("Versuch es weiter\n","Du hast noch", versuche, "Versuche") 
        if versuche == 8:
            print(versuche8)
        elif versuche == 7:
            print(versuche7)
        elif versuche == 6:
            print(versuche6)
        elif versuche == 5:
            print(versuche5)
        elif versuche == 4:
            print(versuche4)
        elif versuche == 3:
            print(versuche3)
        elif versuche == 2:
            print(versuche2)
        elif versuche == 1:
            print(versuche1)
        elif versuche == 0:
            print ("Du hast verloren")
            print(versuche0)
            break
    else:
        print ("Du hast richtig geraten")
    
    

    for buchstabe in tier:
        if buchstabe in erRaten:
            print(buchstabe, end=' ')
        else:                           
            print("_", end=' ')
            gewonnen = False

    if gewonnen == True:
        print("Du hast Gewonnen")
        print("Das Wort ist: ", tier.capitalize())
        break
    print()   
print(tier.capitalize())
