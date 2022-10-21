

from inspect import getargvalues
from multiprocessing.sharedctypes import Value

import random
#Intro
    #Geschichte
    #Befehle
    #aufheben, angreifen, tür, 
    #

class Raum :
    def __init__(self, id , türen, gegenstände, gegner):
        self.id = id
        self.türen = türen
        self.gegenstände = gegenstände
        self.gegner = gegner
        self.erkundet = False
    
    def info(self):
        if len(self.gegner) == 0:
            print("Keine Gegner im Raum")
        for gegner in self.gegner:
            print(gegner.name)
        if self.erkundet:
            print("Raum erkundet")
            if len(self.gegenstände) == 0:
                print("Keine Gegegnstände im Raum")
            for gegenstand in self.gegenstände:
                print(gegenstand.name)
        else:
            print("Raum ist nicht erkundet")
        print("Es gibt Türen zu den Räumen",self.türen)
    

class Enemy :
    def __init__(self, standort, name, gegenstände, leben, angriffswert):
        self.standort = standort
        self.name = name
        self.gegenstände = gegenstände
        self.leben = leben
        self.angriffswert = angriffswert

class Gegenstand:
    def __init__(self, name, gegenstände):
        self.name = name
        self.gegenstände = gegenstände
        
class Waffen(Gegenstand):
    def __init__(self, name, angriffswert):
        super().__init__(name,[]) 
        self.angriffswert = angriffswert
         
class Rüstung(Gegenstand):
    def __init__(self, name, verteidigunswert):
        super().__init__(name, [])
        self.verteidigunswert = verteidigunswert
            
class Zauber(Gegenstand):
    def __init__(self, name, verteidigunswert, angriffswert, heilung):
        super().__init__(name, [])
        self.verteidigunswert = verteidigunswert
        self.angriffswert = angriffswert 
        self.heilung = heilung
        
class Spieler:
    def __init__(self, standort, name, inventar, leben, angriffswert, verteidigunswert):
        self.standort = standort
        self.name = name
        self.inventar = inventar
        self.leben = leben
        self.angriffswert = angriffswert
        self.verteidigunswert = verteidigunswert
        self.rightHand = Waffen("Faust",1)
        self.leftHand = Zauber("ZU DUMM",0,0,0)
        self.rüstung = Rüstung("Hemd",1)
    
    def info(self):
        print("Waffe:",self.rightHand.name)
        print("Rüstung:",self.rüstung.name)
        print("Zauber:",self.leftHand.name)
        print("Inventar:")
        if len(player.inventar) == 0:
            print("Keine Gegegnstände im Inventar")
        for gegenstand in player.inventar:
            print(gegenstand.name)
        

    def aufheben(self, räume):
        raumx = räume[self.standort]
        if len(raumx.gegenstände) == 1:
            gegenstandX = raumx.gegenstände[0]
            self.inventar.append(gegenstandX)
            raumx.gegenstände.remove(gegenstandX)
        elif len(raumx.gegenstände) > 1:
            print("Nice liegt hier viel Zeug rum, welches nehme ich denn mit ?")
            for gegenstand in raumx.gegenstände:
                print(gegenstand.name)
            eingabe = input()
            for gegenstand in raumx.gegenstände:
                if eingabe == gegenstand.name:
                    print("Nehme ich dich mit:", gegenstand.name)
                    self.inventar.append(gegenstand)
                    raumx.gegenstände.remove(gegenstand)
                    break

    
    def angreifen(self, räume):
        raumx = räume[self.standort]
        if len(raumx.gegner) == 1:
            enemyX = raumx.gegner[0]
            schaden = self.angriffswert 
            schaden += self.rightHand.angriffswert
            enemyX.leben = enemyX.leben - schaden
            if enemyX.leben > 0:
                print("Haha du Wurst noch habe ich :",enemyX.leben)
                schaden = enemyX.angriffswert - (self.verteidigunswert + self.rüstung.verteidigunswert)                              
                if schaden > 0: 
                    self.leben = self.leben - schaden
                print(enemyX.name, "Hat dich angegriffen und hat dir Schaden zugefügt", "Du hast noch", self.leben,"Leben") #NOCH NICHT FERTIG wenn selfleben <0

            else:
                print("Gegner besiegt:", enemyX.name)
                raumx.gegner.remove(enemyX)
                
        elif len(raumx.gegner) > 1:
            print("Meine Güte eine Horde Gegner welchen greife ich zuerst an ?")
            for gegner in raumx.gegner:
                print(gegner.name)
            eingabe = input()
            for gegner in raumx.gegner:
                if eingabe == gegner.name:
                    print("Gegner besiegt:", gegner.name)
                    raumx.gegner.remove(gegner)
                    break
                
        return

    def bewegen(self, räume):
        raumx = räume[self.standort]
        if len(raumx.türen) == 1 : # es gibt genau eine tür im raum
            self.standort = raumx.türen[0]
        elif len(raumx.türen) > 1: # mehr als eine tür (keine türen gibt es nicht!)
            print("In welchen Raum willst du?",raumx.türen)
            eingabe = input()
            if int(eingabe) in raumx.türen:
                self.standort = int(eingabe)
            else :
                print("Diese Tür existiert nicht!\n")
        return

    def benutzen(self):
        print("Welchen gegenstand möchtest du benutzen?")
        print("Inventar:")
        for gegenstand in player.inventar:
            print(gegenstand.name)
        eingabe = input()
        nichtGefunden = True
        for gegenstand in self.inventar:
            if eingabe == gegenstand.name:
                nichtGefunden = False
                self.inventar.remove(gegenstand)
                if isinstance (gegenstand, Waffen):
                    self.rightHand = gegenstand
                    print("Waffe angelegt:", self.rightHand.name)
                elif isinstance (gegenstand, Rüstung):
                    self.rüstung = gegenstand
                    print("Rüstung angelegt:", self.rüstung.name)
                elif isinstance (gegenstand, Zauber):
                    self.leftHand = gegenstand
                    print("Zauber angelegt:", self.leftHand.name)
        if nichtGefunden:
            print("Oh gegenstand nicht im Inventar")

    def erkunden(self, räume):
        
        raumx = räume[self.standort]
        if len(raumx.gegner) == 0 & raumx.erkundet == False:
            raumx.erkundet =True
            print("Im Raum hast du",len(raumx.gegenstände),"Gegenstände gefunden")
        elif len(raumx.gegner) > 0:
            print("Es befinden sich Gegner im Raum!!!!!")
        return


def generiere_dungeon():
    raum0 = Raum(0,[1],[Zauber("Feuerball",0,7,0),Zauber("Heilung",0,0,10)],[])
    raum1 = Raum(1,[0,2],[Waffen("Axt",10),Waffen("Schwert",8)],[])
    raum2 = Raum(2,[1],[],[Enemy(2,"Butcher",[],20,6),Enemy(2,"Leshrac",[],24,12),Enemy(2,"Diablo",[],30,15)])
    return [raum0,raum1,raum2]

def generiere_dungeon2():
    raum0 = Raum(0,[1],[],[])
    raum1 = Raum(1,[0,2],[],[])
    raum2 = Raum(2,[1,3],[],[])
    raum3 = Raum(3,[0,2],[],[])
    return [raum0,raum1,raum2,raum3]


def generiere_spieler():
    #spieler1 = spieler
    #spieler1.standort = 0
    #spieler1.name = "Batman"
    #spieler1.inventar = []
    return Spieler(0,"Batman",[],45,5,0)

run = True
actions = 0
    

räume = generiere_dungeon()
player = generiere_spieler() 

# Game-Loop
while  run :
    actions += 1
    print()
    print("Aktion: ",actions)
    print("Du hast die Aktionen:", "aufheben", "benutzen", "angreifen", "erkunden","und", "tür", "zur Verfügung")
    print("_________________________________________________________________________________________")
    # do stuff
    print()
    print(player.name," ist in Raum",player.standort,)
    raumx = räume[player.standort]
    
    # print playerinfo
    player.info()
    print()    
    # print roominfo
    raumx.info()
    print()
    
    # do more stuff
    print("Was willst du tun?\n")
    eingabe = input().lower()

    # more stuff to do?
    if eingabe == "tür" :
        player.bewegen(räume)
    elif eingabe == "angreifen":
        player.angreifen(räume)
    elif eingabe == "erkunden":
        player.erkunden(räume)
    elif eingabe == "benutzen":
        #benutzen = input().lower
        player.benutzen()
        pass
    elif eingabe == "aufheben":
        player.aufheben(räume)
    elif eingabe == "exit" :
        run = False

    