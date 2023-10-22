"""

Skriv et program som spør brukeren om å lage while-løkke som stopper ved input (nok) med liste av venners navn og hvis der finnes Dmitrii printer du "Hyggelig at du husket meg!"

"""

liste = []
navn = "o"

while navn != "nok":
    navn = input("Tast inn navn: ")
    liste.append(navn)
    if "nok" in liste:
        liste.remove(navn)
    print(liste)
if "Dmitrii" in liste:
    print("Hyggelig at du husket meg!")
