from random import randint
from celle import Celle

class Rutenett:
    def __init__(self, rader, kolonner):
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        self._rutenett = self._lag_tomt_rutenett()

    def _lag_tomt_rutenett(self):
        ytre_liste = []
        for i in range(self._ant_rader):
            ytre_liste.append(self._lag_tom_rad())
        return ytre_liste

    def _lag_tom_rad(self):
        liste = []
        for i in range(self._ant_kolonner):
            liste.append(None)
        return liste

    def fyll_med_tilfeldige_celler(self):
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                self.lag_celle(rad, kol)

    def lag_celle(self, rad, kol):
        inst_var = Celle()
        ny_celle = randint(0,2)
        if ny_celle == 0:
            inst_var.sett_levende()
        self._rutenett[rad][kol] = inst_var


    def hent_celle(self, rad, kol):
        if 0<=rad<=self._ant_rader and 0<=kol<=self._ant_kolonner:
            return self._rutenett[rad][kol]
        else:
            return None

    def tegn_rutenett(self):
        for i in range(len(self._rutenett)):
            for j in range(len(self._rutenett[i])):
                print(self.hent_celle(i, j).hent_status_tegn(), end = "")

    def _sett_naboer(self, rad, kol):
        pass
        # self._rutenett[rad][kol] = Celle()
        start_celle = self.hent_celle(rad,kol)


        nabo1 = self.hent_celle(rad-1,kol-1)
        # print(nabo1)
        if nabo1 is not None:
            return start_celle.legg_til_nabo(nabo1)
        else:
            return None

        nabo2 = self.hent_celle(rad-1, kol)
        # print(nabo2)
        if nabo2 is not None:
            start_celle.legg_til_nabo(nabo2)
        else:
            None

        nabo3 = self.hent_celle(rad-1, kol+1)
        # print(nabo3)
        if nabo3 is not None:
            start_celle.legg_til_nabo(nabo3)
        else:
            None

        nabo4 = self.hent_celle(rad,kol-1)
        # print(nabo4)
        if nabo4 is not None:
            start_celle.legg_til_nabo(nabo4)
        else:
            None

        nabo5 = self.hent_celle(rad, kol+1)
        # print(nabo5)
        if nabo5 is not None:
            start_celle.legg_til_nabo(nabo5)
        else:
            None

        nabo6 = self.hent_celle(rad+1, kol-1)
        # print(nabo6)
        if nabo6 is not None:
            start_celle.legg_til_nabo(nabo6)
        else:
            None

        nabo7= self.hent_celle(rad+1, kol)
        # print(nabo7)
        if nabo7 is not None:
            start_celle.legg_til_nabo(nabo7)
        else:
            None

        nabo8 = self.hent_celle(rad+1, kol+1)
        # print(nabo8)
        if nabo8 is not None:
            start_celle.legg_til_nabo(nabo8)
        else:
            None

    def koble_celler(self):
        pass

    def hent_alle_celler(self):
        pass

    def antall_levende(self):
        pass
