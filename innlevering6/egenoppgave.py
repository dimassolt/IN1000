# Lag et program som henter Bakugans navn, farge, krefter(int!) (f.eks. Drago, rod, 950G)
# fra brukeren og bruker de til aa sammenligne med annen Bakugan som er gitt tidligere Neo Dragonoid, svart, 490G.
# Lag klassen til aa hente alle Bakugans egenskaper. Hvis krefter av den inputs Bakugan er svakere enn paa den som
# er gitt, skal inputs Bakugan tape.
# Hvis omvendt, skal inputs Bakugan vinne. Hvis like, "tegne"
# Lag gjerne testeprogramm som kjører med klassen

class Bakugan():
    def __init__(self, navn, farge, krefter):
        self._navn = navn
        self._farge = farge
        self._krefter = krefter
    def battle(self):

        n = input("Oppgi Bakugans navn: ")
        f = input("Oppgi Bakugans farge: ")
        k = int(input("Oppgi Bakugans krefter: "))
        bakugan_navn = ("Din Bakugan: "+ n+ " " +f+ " " + str(k) + "G" )
        if k < self._krefter:
            print(bakugan_navn, "har tapt, dessverre(")
        elif k > self._krefter:
            print(bakugan_navn, " har vunnet!")
        elif k == self._krefter:
            print("Tegne!")
