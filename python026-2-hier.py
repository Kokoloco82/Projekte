from ast import If
from os import sep
from re import M
from webbrowser import get
from xml.dom.pulldom import END_ELEMENT


tierListe = {
    "Asien": {  "Elefant": "Gräsern, Laub und Weichholz",
                "Muntjak": "Gräser Blätter und Knospen"
                },

    "Afrika": { "Löwe": "Hauptsächlich Huftiere wie Gazellen, Zebras etc.",
                 "Chinesischer-muntjak": "Gräser Blätter und Knospen"
                 },    

    "Nordamerika": { "Bär": "Hauptsächlich Säugetiere, Vögel, Fische.",
                    "Aberthörnchen":"Samen, Knospen, Pilze etc"
                    },                
                     
    "Südamerika":  { "Papagei": "Samen, Beeren, Früchten, Blüten etc.",
                     "Jaguar": "Schildkröten, Tapire, Vögel etc."
                     },                 
                                 
     "Europa":   { "Alpenmurmeltier": "Kräuter und Gräser, vor allem Blätter und Blüten, aber auch Körner",
                    "Europäische-mufflons": "Moosen, Flechten, Baumrinden etc."},  

    "Australien": { "Koala":"Kräuter und Gräser, vor allem Blätter und Blüten",
                    "Känguru": "Obst und Gemüse und knabbern an Baumrinde."}
                    }                       

kontinentListe = ["Asien", "Afrika", "Nordamerika", "Südamerika", "Europa", "Australien"]

hello = "Hallo User, wenn Sie das programm Ende wollen, geben Sie bitte 'Ende' ein, oder wenn sie züruck wieder von den Tieren nach den Kontimenten Optionen gehen, geben sie bitte 'Back' ein.\n"
print(hello)

while True:
        for i in kontinentListe:
                print(i)
        print("\n")

        kontinent = input("Gib bitte ein Kontinent ein: ").capitalize()
        print("\n")
        if kontinent == "Ende":
                break

        while not kontinent in kontinentListe:
                kontinent = input("Gib bitte ein Kontinent ein: ").capitalize()
                print()
        for i, n in tierListe[kontinent].items():   # i ist das key vom Kontinent und n ist das value
                print(i)
        print("\n")

        tiere = ""
        tierWahl = input("Suche bitte das Tier aus: \n").capitalize()

        print("\n")

        while (tierWahl != None) and (tierWahl != "Back") : 
                tiere = tierListe.get(kontinent).get(tierWahl)
                if tiere == None:
                        print("Gib bitte eine eine Option aus den verfügbaren Optionen!!! \n")    
                        tierWahl = input("Suche bitte das Tier aus: \n").capitalize()
                else:
                        print("Die Nahrung von", tierWahl, " ist " , tiere)
                        print("\n")
                        break
        


