from sang import Sang
class Spilleliste:

    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def les_fil(self,filnavn):
        musique = open(filnavn)
        for linje in musique:
            alle_data = linje.strip().strip(";").split(";")
            self._sanger.append(Sang(alle_data[1], alle_data[0]))

    def __str__(self):
        return self._sanger

    def legg_til_sang(self, ny_sang):
        self._sanger.append(ny_sang)

    def fjern_sang(self, sang):
        self._sanger.remove(sang)

    def finn_sang(self, tittel):
        for indeks in self._sanger:
            sjekk = indeks.sjekk_tittel(tittel)
            if sjekk == True:
                return indeks

        return None

    def hent_artist_utvalg(self, artistnavn):
        ny_list = []
        for indeks in self._sanger:
            if indeks.sjekk_artist(artistnavn) == True:
                ny_list.append(indeks)
        return ny_list

    def spill_sang(self,sang):
        sang.spill()

    def spill_alle(self):
        for indeks in self._sanger:
            indeks.spill()

# Nede er testeprogram som ble brukt til å sjekke noen punkter

# a = Spilleliste("Hele musikkbiblioteket")
# a.les_fil("musikk.txt")
# a.hent_artist_utvalg("Queen")
# a.legg_til_sang("Californication; Red Hot Chily Peppers")
# a.__str__()
# a.spill_alle()
