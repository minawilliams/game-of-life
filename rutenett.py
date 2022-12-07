from random import randint
from celle import Celle

#improterer klassnene randit og celle

class Rutenett:
    def __init__(self, rader, kolonner): #klassen rutenett har føgende instansvariabler
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        self._rutenett = self._lag_tomt_rutenett() #instansen rutenett kaller på metode som lager rutenett

    def _lag_tom_rad(self):
        inne_liste = [] #liste for rader i rutenettet
        for repetisjoner in range(self._ant_kolonner):
            inne_liste.append(None) #legger til none i hver kolonne i lista
        return inne_liste


    def _lag_tomt_rutenett(self):
        ytre_liste =[] #lager ny liste
        for rader in range(self._ant_rader): #kolonnen vi lagde i metoden over skal settes sammen etter gitt antall rader
            ytre_liste.append(self._lag_tom_rad())
        return ytre_liste #returnerer en nøstet liste


    def fyll_med_tilfeldige_celler(self): #for hver plass i rutenettt skal det oppretetes et celleobjekt
        for rad_nr in range(self._ant_rader): #metoden itererer gjennom hver rad
            for kol_nr in range(self._ant_kolonner): #for å så iterere gjennom hver kolonne
                self.lag_celle(rad_nr, kol_nr) #for hver plass skal det lages en celle


    def lag_celle(self, rad, kol): #lager celleobjekt, 33% sjanse for levende
        celle = Celle()
        tall = randint(0,2)
        if tall == 0: #hvis det tilfeldige tallet ble 0, blir cellens status satt til levende
            celle.sett_levende()
        self._rutenett[rad][kol] = celle #legger cellen til i rutenettet


    def hent_celle(self, rad, kol): #henter ut cellen hvis kordinater er innenfor rutenettet
        if rad >= self._ant_rader or kol >= self._ant_kolonner or kol < 0 or rad < 0:
            return None
        return self._rutenett[rad][kol]


    def tegn_rutenett(self): #printer rutenett
        for rad in self._rutenett:
            for celle in rad:
                print(celle.hent_status_tegn(), end = " ")
            print()


    def _sett_naboer(self, rad, kol):
        meg= self.hent_celle(rad, kol) #en celle kan ikke være sin egen nabo
        for rader in range(-1,2): #naboenes kordinater har et spenn mellom -1 til 2
            for kolonner in range(-1,2):
                if not(rader == 0 and kolonner == 0): #hvis ikke objektet er den bestemte cellen
                    nabo=self.hent_celle(rad + rader, kol + kolonner)
                    if nabo is not None:
                        meg._naboer.append(nabo) #legger inn naboer i listen til cellen


    def koble_celler(self):
        for rader in range(self._ant_rader): #cellenes naboer blir opprettet
            for kolonner in range(self._ant_kolonner):
                self._sett_naboer(rader, kolonner)


    def hent_alle_celler(self): #legger alle cellene i en liste
        antall_celler=[]
        for rad in range(self._ant_rader): #itererer gjennom rutenettet:
            for kol in range(self._ant_kolonner):
                antall_celler.append(self.hent_celle(rad, kol)) #legger til cellene med kordinater inn i listen
        return antall_celler


    def antall_levende(self): #teller ant levende ved å kalle på metoden som sjekker status
        levende=0 #ant levende satt til 0
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                if self.hent_celle(rad, kol).er_levende():
                    levende+=1 #for hver gang programmet kjører gjennom løkken går ant levende opp
        return levende #returnerer ant levende
