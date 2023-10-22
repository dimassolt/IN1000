#Punkt 1
class Hund():

    def __init__(self, alder, vekt):
        self._alder = alder
        self._vekt = vekt
        self._metthet = 10
    # def hent_metthet(self):
    #     return self._metthet
    # def hent_mengde_av_mating(self):
    #     return self._mengde_av_mating
#Punkt 3
    def hent_alder(self):
        return self._alder
    def hent_vekt(self):
        return self._vekt
#Punkt 4
    def spring(self):
        self._metthet -= 1
        if self._metthet < 5:
            self._vekt -= 1
            # return self._metthet

#Punkt 5
    def spis(self, mengde_av_mating):
        self._metthet += mengde_av_mating
        if self._metthet > 7:
            self._vekt += 1
