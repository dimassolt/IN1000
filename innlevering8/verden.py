from rutenett import Rutenett
from celle import Celle
class Verden:
    def __init__(self, rader, kolonner):

        self._rutenett = Rutenett(rader, kolonner)
        self._generasjonsnummer = 0

    def tegn(self):
        self._generasjonsnummer +=1
        print(self._generasjonsnummer)
         # self._rutenett and self._generasjonsnummer
    def oppdatering(self):

        # if self._rutenett:
        self._rutenett.levende_naboer()
