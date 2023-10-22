#Punkt 1
class Motorsykkel():

    def __init__(self, merke, nummer):
        self._kilometerstrand = 0
        self._merke = merke
        self._nummer = nummer
#Punkt 3
    def hent_kilometerstrand(self):
        return self._kilometerstrand
#Punkt 2
    def kjor(self, km):
        self._kilometerstrand += km
#Punkt 6
    def skriv_ut(self):
        print(self._merke, "med nummeret:", self._nummer, "har kjørt:", self._kilometerstrand, "km.")
