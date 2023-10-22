# I denne oppgaven bør du lage en fil som består av telefonbok med navn som nøkkelverdi og telefonnummer som verdi.
# Etterpaa skal du skrive et program som kaller funksjon. Den funksjonen skal tar inn  fil som argument.
# Den funksjonen skal tar inn navn fra input fra brukeren og programet returnerer tlf nr hvis den personen finnes i filen.

ordbok = {}
telefonbok = open("telefon.txt")
def allo_allo(telefonbok):
    for linje in telefonbok:
    # print(ordbok)
    hvem = input("Print navnet fra telefonbok: ")
    if hvem in ordbok.keys():
        tlf = ordbok[hvem]
        print("Her er telefonnummer: "+ tlf + " til " + hvem)
    else:
        print("Denne personen finnes ikke i telefonboka")

    return ordbok
allo_allo(telefonbok)
