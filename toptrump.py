import random
# cards = {'Bob': [1, 3, 6, 5], 'Dave': [1, 8, 5, 5], 'Steve': [1, 3, 9, 7], 'John': [6, 7, 9, 5], 'Bill': [7, 3, 9, 1], 'Rodger': [4, 5, 2, 8]}
# player = {name: cards[name] for name in random.sample(cards.keys(), len(cards) // 2)}
# computer = {name: cards[name] for name in cards.keys() - player.keys()}
# print(player)
# print(computer)
# {'Bob': [1, 3, 6, 5], 'John': [6, 7, 9, 5], 'Rodger': [4, 5, 2, 8]}
# {'Steve': [1, 3, 9, 7], 'Dave': [1, 8, 5, 5], 'Bill': [7, 3, 9, 1]}
# spielerDeck = []
# tiereList = []
# cpuDeck = []
# class Karten:
#         def __init__(self, name, leben, ausdauer, stärke, höhe, länge):
#                 self.name = name
#                 self.leben = leben
#                 self.ausdauer = ausdauer
#                 self.stärke = stärke
#                 self.höhe = höhe
#                 self.länge = länge
#                 tiereList.append(self)
# katze = Karten ("Katze",20,25,15,20,30)
# hund = Karten ("Hund",15,30,25,60,45)
# maus = Karten ("Maus",5,15,5,5,5)
# hase = Karten ("Hase",5,10,0,5,10)
# pferd = Karten ("Pferd",10,25,30,100,100)
# ratte = Karten ("Ratte", 10,5,10,10,10)

# kartenTalente = ['leben', 'ausdauer', 'stärke', 'höhe', 'länge']
# def printTiereListeTalente(kartenTalente):
#         print ("* Name ********* Leben ********* Ausdauer ********* Stärke ********* Höhe ********* Länge **")
#         print ("—————————————————————————————————————————————–")
#         for tier in kartenTalente:
#                 col_1 = "*************"
#                 col_1 = col_1.replace("*", tier.name + " ",1)
#                 col_1 = col_1[:14]
#                 col_2 = "**************"
#                 col_2 = col_2.replace("*", str(tier.leben) + " ",1)
#                 col_2 = col_2[:16]
#                 col_3 = "*******************************************"
#                 col_3 = col_3.replace("*", str(tier.ausdauer) + " ",1)
#                 col_3 = col_3[:17]
#                 col_4 = "**************************"
#                 col_4 = col_4.replace("*", str(tier.stärke) + " ",1)
#                 col_4 = col_4[:18]
#                 col_5 = "****************"
#                 col_5 = col_5.replace("*", str(tier.höhe) + " ",1)
#                 col_5 = col_5[:18]
#                 col_6 = "****************************"
#                 col_6 = col_6.replace("*", str(tier.länge) + " ",1)
#                 col_6 = col_6[:16]
#                 data_length = (len(tier.name) + len(str(tier.leben)) + len(str(tier.ausdauer)) + len(str(tier.stärke)) + len(str(tier.höhe)) + len(str(tier.länge)))
#                 print ("*", col_1 + "|" + col_2, col_3, col_4, col_5, col_6,)
#                 print (" ")

# def spielerZug():
#         def spieler1draw():
#                 spieler1draw = input("Wähle eine Rasse aus!")
#                 return str(spieler1draw)
#         karteGezogen = False
#         while karteGezogen == False:
#                 spieler1draw = spieler1draw()
#                 if spieler1draw in tiereList:
#                         spieler1draw = tiereList[spieler1draw]
#                         if spieler1draw in spielerDeck:
#                                 karteGezogen = True
#                         else:
#                                 pass
#                 else:
#                         print ("Invalid card. Please re-enter")


# class Spieler:
#     def __init__(self):
#         self.name = input(self.name)
#         self.rightHand = self.Karten("Hand")
        
#         pass

#     def info(self):
#             print("Spieler:",self.name)
#             print("Karte:",self.Karten.name)
#             print("Tier:",self.Tier.name)
#             print("Talent:")
#             if len(Spieler.rightHand) == 0:
#                 print("Keine Karte in der Hand")
#             for Karten in Spieler.rightHand:
#                 print(Karten.name)

# def generiere_spieler(self):
#     tischX = Tisch[self.standort]
#     spieler1.standort = 0
#     spieler1.name = Spieler.name
#     spieler1.rightHand = []
#     spieler1 = input(Spieler.name)
#     return Spieler("Spieler1: ",Spieler.name)

# def generiere_spieler(self):
#     tischX = Tisch[self.standort]
#     spieler2.standort = 0
#     spieler2.name = Spieler.name
#     spieler2.leftHand = []
#     spieler2 = input(Spieler.name)
#     return Spieler("Spieler2: ", Spieler.name)

# def generiere_kiGegner(self):
#     spielTischX = Tisch[self.standort]
#     spielerKI.standort = 0
#     spielerKI.name = "Babajaga"
#     spielerKI.middleHand = []
#     spielerKI = spielerKI.name
#     return Spieler("Computer:", "Babajaga")

# def random_asign(deck):
#        if len(tiereList) == 0:
#                print ("Karten verteilen")
#        else:
#                while len(deck) < 5:
#                        temp = random.choice(tiereList)
#                        if temp in deck:
#                                pass
#                        else:
#                                deck.append(temp)
#                                tiereList.remove(temp)
#                if deck == spielerDeck:
#                        print ("Your deck updated: ")
#                        print (deck[0].name, "|", deck[1].name, "|", deck[2].name, "|", deck[3].name, "|", deck[4].name, "|")


# class mainMenu:
#     def __init__(self):
#         pass

# def generiere_spielMenu():
#     print("Mit wieviel Spielern möchtest du Spielen:")
#     eingabe = input("1", "2")
#     print("Möchtest du das Spiel Beenden")
#     eingabe = input("Ja?, dann schreibe exit")
#     Exit = exit
#     return [mainMenu]



# def generiere_tisch():
#     tisch0 = Tisch(0,[],[],[])
#     tisch1 = Tisch(0,[],[],[])
#     tisch2 = Tisch(0,[],[],[])
#     return [tisch0,tisch1,tisch2]

# class Tisch :
#     def __init__(self, id , tisch, karten, gegenspieler):
#         self.id = id
#         self.tisch = tisch
#         self.karten = karten
#         self.gegenspieler = gegenspieler
#         self.erkundet = False
    
#     def info(self):
#         if len(self.gegenspieler) == 0:
#             print("Keine Gegenspieler im Raum")
#         for gegenspieler in self.gegenspieler:
#             print(gegenspieler.name)
#         print("Es gibt andere Spieltische",self.tisch)




# class Tiere:
#     def __init__(self):
#         self.name
#         pass

# class Katzen(Tiere):
#     def __init__(self):
#         super().__init__()
#         self.name

# class Hunde(Tiere):
#     def __init__(self):
#         self.name
#         super().__init__()

# run = True
# actions = 0

# Tisch = generiere_tisch(self)
# player = generiere_spieler(self) 

#Gameloop
