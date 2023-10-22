#Punkt 1
a = "s"

def lagBrukernavn(navn):
    navn = input("Oppgi full navnet ditt: ")
    if navn != "wwee":
        navn = navn.lower()
        navn.split(" ")
        # print(navn.split(" "))
        fornavn = navn.split(' ')
        # print(fornavn[0])
        etternavn = navn.find(" ")
        etternavn = etternavn + 1
        # print(navn[etternavn])
        print("")
        navn = fornavn[0] + navn[etternavn]
        print("Her er ditt brukernavn: ", navn)

    return navn

lagBrukernavn(a)

#Punkt2
a = input("Oppgi ditt brukernavn: ")
b = input("Oppgi e-post suffix, (det som står etter @): ")
def lagEpost(brukernavn,epost_suffix):
    print("")
    a = brukernavn
    b = epost_suffix
    result = brukernavn + "@" + epost_suffix
    print("")
    print("Her er e-postadressen din: ", result)
    print("")
    return result
lagEpost(a,b)


#Punkt 3

ordbok = {"olan": "ifi.uio.no", "karin": "student.matnat.uio.no", "iulp": "sweet.home.no"}
def skrivUtEposter(ordbok):
    for name in ordbok.items():
        a = name[0]
        b = name[1]
        # print("Det som vi faar i punkt 3: ")
        lagEpost(a,b)

skrivUtEposter(ordbok)

#Punkt 4

tom_ordbok = {}
while len(tom_ordbok) < 100000:
    kondisjon = input("Tast inn ""i"" som starter programmet: ")
    if kondisjon == "i":
        navn = "e"
        brukernavn = lagBrukernavn(navn)
        print(brukernavn)
        suffix = input("Tast inn epost suffix: ")
        tom_ordbok[brukernavn] = suffix
        print(tom_ordbok)
        kondisjon = input("Hva gjør vi videre?: ")
        if kondisjon == "p":
            skrivUtEposter(tom_ordbok)
        elif kondisjon == "s":
            print("Du valgte å slutte programmet!")
            break
