class Celle:
    # Konstruktør
    def __init__(self):
        self._status = "doed"
        self._naboer = [] #tom liste
        self._ant_levende_naboer = 0

    def sett_doed(self): #setter status til død
        self._status = "doed"

    def sett_levende(self): #setter status til levende
        self._status = "levende"


    def er_levende(self): #sjekker om cellen er levende
        if self._status == "levende":
            return True
        else:
            return False

    def hent_status_tegn(self): #avgjør cellens utseende basert på liv
        if self.er_levende():
            return "O"
        else:
            return "."

    def legg_til_nabo(self, nabo): #legger til celle i naboliste
        self._naboer.append(nabo)


    def hent_status(self):
        return self.status


    def tell_levende_naboer(self):
        self._ant_levende_naboer = 0 #nullstiller løkka
        for nabo in self._naboer: #itererer gjennom cellene i nabolista
            if nabo.er_levende() == True: #hvis cellen er levende går telleren opp
                self._ant_levende_naboer += 1

    def oppdater_status(self): #setter livstilstanden til cellen etter spillerreglene
        if self._status == "levende":
            if self._ant_levende_naboer <= 1:
                self.sett_doed()
            if self._ant_levende_naboer > 3:
                self.sett_doed()


        if self._status == "doed":
            if self._ant_levende_naboer == 3:
                self.sett_levende()
