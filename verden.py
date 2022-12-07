from rutenett import Rutenett #importerer klassen rutenett

class Verden:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner

        self._rutenett = rutenett = Rutenett(rader, kolonner) #rutenettet blir definert med ant rader og kolonner
        self._rutenett.fyll_med_tilfeldige_celler() #rutenettet fylles med celler
        self._rutenett.koble_celler() #deretter kobles cellenes naboer sammen

        self._generasjonsnummer = 0 #gennr starter på 0 ved opprettelse av verdenen.


    def tegn(self):
        self._rutenett.tegn_rutenett() #ruteneettet printes i temrinalen
        print("generasjonsnummer: ", self._generasjonsnummer) #gennrummer
        print("antall levende: ", self._rutenett.antall_levende()) #kaller på metoden som teller levende celler


    def oppdatering(self):
        self._rutenett.antall_levende() #teller antall levende celler i rutenettet
        for celle in self._rutenett.hent_alle_celler(): #alle cellene i rutenettet legges til en liste
            celle.tell_levende_naboer() #for disse skal man telle ant levende naboer
            celle.oppdater_status() #statusen til cellen blir oppdatert etter retingslinjene i oppdater status-metoden
        self._generasjonsnummer += 1 #for hver gang oppdateringen bli kalt på, øker gennummer med +1
