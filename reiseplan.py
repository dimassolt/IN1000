#punkt 1
steder = []
sted = input("Tast inn sted: ")
steder.append(sted)
for sted in steder:
    sted = input("Tast inn sted: ")
    steder.append(sted)
    if len(steder) == 5:
        break
print(steder)

#punkt2
klaer = []
klesplagg = input("Tast inn klesplagg: ")
klaer.append(klesplagg)
for klesplagg in klaer:
    klesplagg = input("Tast inn klesplagg: ")
    klaer.append(klesplagg)
    if len(klaer) == 5:
        break
print(klaer)

datoer = []
dato = input("Tast inn avreisedato: ")
datoer.append(dato)
for dato in datoer:
    dato = input("Tast inn avreisedato: ")
    datoer.append(dato)
    if len(datoer) == 5:
        break
print(datoer)

#punkt3

reiseplan = [steder + klaer + datoer]
print(reiseplan)

#punkt 4
for steder in reiseplan:
    print(steder)
# for klaer in reiseplan:
#     print(klaer)
# for datoer in reiseplan:
#     print(datoer)

#punkt5

liste_indeks1 = int(input("Hvilken list trenger du? (0 - sted, 1 - klaer, 2 - datoer) "))
liste_indeks2 = int(input("Hvilken element trenger du? (0 - 1, 1 - 2, 2 - 3 ...) "))
if 0<=liste_indeks1<=2:
    if 0<=liste_indeks2<=4:
        print(reiseplan[liste_indeks1][liste_indeks2])
    else:
        print("Ugyldig input!")
else:
    print("Ugyldig input!")
