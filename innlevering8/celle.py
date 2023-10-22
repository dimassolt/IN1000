class Celle:
    # Konstruktør
    def __init__(self):
        self._status = "doed"
        self._naboer = []
        self._ant_levende_naboer = 0

    def sett_doed(self):
        self._status = "doed"
        # return self._status

    def sett_levende(self):
        self._status = "levende"
        # return self._status

    def er_levende(self):
        if self._status == "levende":
            return True
        else:
            return False

    def hent_status_tegn(self):
        if self.er_levende() == True:
            return "O"
        else:
            return "."

    def legg_til_nabo(self, nabo):
        self._naboer.append(nabo)

    def tell_levende_naboer(self):
        self._ant_levende_naboer = 0
        for beboer in self._naboer:
            if beboer.er_levende() == True:
                self._ant_levende_naboer += 1

    def oppdater_status(self):
        if self._status == "levende" and self._ant_levende_naboer < 2:
            self.sett_doed()
        elif self._status == "levende" and (self._ant_levende_naboer == 2 or self._ant_levende_naboer == 3):
            self.sett_levende()
        elif self._status == "levende" and self._ant_levende_naboer > 3:
            self.sett_doed()
        elif self._status == "doed" and self._ant_levende_naboer == 3:
            self.sett_levende()
# s = Celle()
# s.sett_doed()
# s.sett_levende()
# s.er_levende()
# s.hent_status_tegn()
# s.legg_til_nabo(1)
# s.tell_levende_naboer()
