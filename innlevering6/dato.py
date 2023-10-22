#Punkt 1
class Dato():

    def __init__(self, ny_dag, ny_maaned, nytt_aar):
        self._ny_dag = ny_dag
        self._ny_maaned = ny_maaned
        self._nytt_aar = nytt_aar
    def hent_aar(self):
        return self._nytt_aar
    def hent_str_dato(self):    #, ny_dag, ny_maaned, nytt_aar):
        self._ny_dag = input("Oppgi en dag: ")

        # return ny_dag
        self._ny_maaned = input("Oppgi en maaned: ")
        # return ny_maaned
        self._nytt_aar = input("Oppgi et aar: ")
        # return nytt_aar
        return self._ny_dag, self._ny_maaned, self._nytt_aar
        # return ("Her er datoen: ", self._ny_dag + "." + self._ny_maaned + "." + self._nytt_aar )
    def sjek(self):
        if self._ny_dag == "15":
            print("Loenningsdag!")
        elif self._ny_dag == "1":
            print("Ny maaned - nye muligheter!")
