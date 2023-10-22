class Sang:

    def __init__(self, artist, tittel):
        self._artist = artist
        self._tittel = tittel

    def spill(self):
        print("Spiller "+"'", self._tittel, "'"+" av " + "'", self._artist ,"'")
        # return "Spiller "+ self._tittel +" av " + self._artist

    def sjekk_artist(self, navn):
        listt = navn.split() + self._artist.split()
        #her sjekker vi at lengden er samme eller forskjellige
        #vi adderer navn fra testeprogramm til self._artist fra testeprogramm
        if len(set(listt)) < len(listt):
            return True
        else:
            return False

        print(list)
        print(set(list))

    def sjekk_tittel(self, tittel):
        var1 = tittel.lower().strip()
        var2 = self._tittel.lower().strip()
        if var1 == var2:
            return True
        else:
            return False

    def sjekk_artist_og_tittel(self,artist,tittel):
        if (artist in self._artist or artist == self._artist) and self._tittel == tittel:
            return True
        else:
            return False

    def __str__(self):
        return f'Spiller " " " {self._tittel} " " "   av   " " " {self._artist} """ \n '

#Nede er testeprogram som ble brukt til å sjekke noen punkter

# def testprogram():
#     test = Sang("Lady Gaga and Bradley Cooper", "come on")
# #     # print(test.spill())
# #     test.sjekk_artist("Sadley")
#     test.sjekk_tittel("Comeon")
# # #     test.sjekk_artist_og_tittel("Lady Gaga and Bradley Cooper","come on")
# testprogram()
