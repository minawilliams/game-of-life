from verden import Verden #importerer klassen verden

def hovedprogram():
    rad = int(input("tast antall rader for spillebrett: "))
    kol = int(input("tast antall kolonner for spillbrett "))

    verden = Verden(rad, kol) #opprettter verden-objekt med brukers input
    verden.tegn()  #tegner verdenen-objektet i terminalen basert på brukers input

    while True: #hvis bruker taster et blankt input kjøres løkken
        if not input ("trykk ENTER for aa fortsette, q for aa avslutte programmet "):
            print("oppdatering():")
            verden.oppdatering() #verdenen blir oppdatert
            verden.tegn() #den nye generasjonen skrives i terminalen
            
        else: #hvis bruker taster q eller noe annet avlusttes programmet
            print("avlutter programmet")
            exit()


# starte hovedprogrammet
hovedprogram()
