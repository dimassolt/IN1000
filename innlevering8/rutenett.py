from random import randint
from celle import Celle

class Rutenett:
    def __init__(self, rader, kolonner):
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        self._rutenett = self._lag_tomt_rutenett()

    def _lag_tomt_rutenett(self):
        ytre_liste = []
        for hver_kolonne in range(self._ant_rader):
            ytre_liste.append(self._lag_tom_rad())
        return ytre_liste

    def _lag_tom_rad(self):
        inne_liste = []
        for hver_rad in range(self._ant_kolonner):
            inne_liste.append(None)
        return inne_liste

    def fyll_med_tilfeldige_celler(self):
        for raden in range(self._ant_rader):
            for kolonnen in range(self._ant_kolonner):
                self.lag_celle(raden, kolonnen)

    def lag_celle(self, rad, kol):
        celle = Celle()
        random = randint(1,3)
        if random == 1:
            celle.sett_levende()
        else:
            celle.sett_doed()
        self._rutenett[rad][kol] = celle

    def hent_celle(self, rad, kol):
        if rad in range(self._ant_rader) and kol in range(self._ant_kolonner):
            return self._rutenett[rad][kol]
        else:
            return None

    def tegn_rutenett(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        for alle_rader in range(len(self._rutenett)):
            for alle_kolonner in range(len(self._rutenett[alle_rader])):
                print(self.hent_celle(alle_rader, alle_kolonner).hent_status_tegn(), end = "")

            print(end="\n")

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    def _sett_naboer(self, rad, kol):

        start_celle = self.hent_celle(rad,kol)
        # print(start_celle)
        nabo1 = self.hent_celle(rad-1,kol-1)
        # print(nabo1)

        # print(nabo1)
        if nabo1 is not None:
            start_celle.legg_til_nabo(nabo1)
        #
        # else:
        #      start_celle.legg_til_nabo(None)

        nabo2 = self.hent_celle(rad-1, kol)
        # print(nabo2)
        if nabo2 is not None:
            start_celle.legg_til_nabo(nabo2)
        # else:
        #     start_celle.legg_til_nabo(None)

        nabo3 = self.hent_celle(rad-1, kol+1)
        # print(nabo3)
        if nabo3 is not None:
            start_celle.legg_til_nabo(nabo3)
        # else:
        #     start_celle.legg_til_nabo(None)

        nabo4 = self.hent_celle(rad,kol-1)
        # print(nabo4)
        if nabo4 is not None:
            start_celle.legg_til_nabo(nabo4)
        # else:
        #     start_celle.legg_til_nabo(None)

        nabo5 = self.hent_celle(rad, kol+1)
        # print(nabo5)
        if nabo5 is not None:
            start_celle.legg_til_nabo(nabo5)
        # else:
        #     start_celle.legg_til_nabo(None)

        nabo6 = self.hent_celle(rad+1, kol-1)
        # print(nabo6)
        if nabo6 is not None:
            start_celle.legg_til_nabo(nabo6)
        # else:
        #     start_celle.legg_til_nabo(None)

        nabo7= self.hent_celle(rad+1, kol)
        # print(nabo7)
        if nabo7 is not None:
            start_celle.legg_til_nabo(nabo7)
        # else:
        #     start_celle.legg_til_nabo(None)

        nabo8 = self.hent_celle(rad+1, kol+1)
        # print(nabo8)
        if nabo8 is not None:
            start_celle.legg_til_nabo(nabo8)
        # else:
        #     start_celle.legg_til_nabo(None)



    def koble_celler(self):
        for i in range(self._ant_rader):
            for j in range(self._ant_kolonner):
                self._sett_naboer(i,j)

    def hent_alle_celler(self):

        listen_med_alle_inst_av_klassen_Celle = []
        for i in range(len(self._rutenett)):
            for j in range(len(self._rutenett[i])):
                celle_inst = self.hent_celle(i,j)
                listen_med_alle_inst_av_klassen_Celle.append(celle_inst)
        return listen_med_alle_inst_av_klassen_Celle


    def antall_levende(self):
        counter = 0

        for rad in range(len(self._rutenett)):
            for kol in range(len(self._rutenett[rad])):
                celle_skal_sjekkes = self.hent_celle(rad,kol)
                if celle_skal_sjekkes.er_levende() == True:
                    counter +=1
                else:
                    counter +=0
        return counter
