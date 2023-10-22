class Person:
    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder
    def __str__(self):
        return self._navn

    def hent_navn(self):
        return self._navn

    def __eq__(self, annen_person):
        if self._navn == annen_person.hent_navn():
            return True
        else:
            return False
    # def __repr__(self):

ola = Person("Ola",10)
print(ola)
