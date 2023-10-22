#Punkt 1 og punkt 2 og 5
# a = 2
# b = 5

def addisjon(tall1,tall2):
    return(tall1+tall2)


# add = addisjon(a,b)
# assert add == 7
# print(add)


def subtraksjon(tall1,tall2):
    return(tall2-tall1)
# sub = sx`ubtraksjon(a,b)
# assert sub == 3
# print(sub)


def divisjon(tall1,tall2):
    return(tall1/tall2)
# div = divisjon(a,b)
# assert div == 0.4
# print(div)

"""
# def utregninger():
#     a = float(input("Oppgi tall1: "))
#     b = float(input("Oppgi tall2: "))
#     if b != 0:
#         add = addisjon(a,b)
#         sub = subtraksjon(a,b)
#         div = divisjon(a,b)
#     print("")
#     print("Resultatet av addisjon: ", add)
#
#     print("Resultatet av subtraksjon: ", sub)
#     print("Resultatet av divisjon: ", div)
#     print("")
#
# utregninger()
"""

# Punkt 3

# antallTommer = 1
def tommerTilCm(antallTommer):
    assert antallTommer > 0
    antallCm = antallTommer*2.54
    z = 0
    return antallCm

# Tommer_Cm = tommerTilCm(2)
# print(Tommer_Cm, "cm")

def skrivBeregninger():
    print("Utregninger:")
    a = float(input("Oppgi tall1: "))
    b = float(input("Oppgi tall2: "))
    if b != 0:
        add = addisjon(a,b)
        sub = subtraksjon(a,b)
        div = divisjon(a,b)

    print("")
    print("Resultatet av addisjon: ", add)

    print("Resultatet av subtraksjon: ", sub)
    print("Resultatet av divisjon: ", div)
    print("")
    print("Konvertering fra tommer til cm:")

    Tc = 1
    if Tc !=0:
        Tc = float(input("Oppgi et tall i tommer til å konvertere det i cm: "))
    antallCm = tommerTilCm(Tc)
    print("")
    print("Resultatet: ", antallCm)
skrivBeregninger()
