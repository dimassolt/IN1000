"""

Programmet gir feil hvis vi definerer ikke variabel "a" før prosedyren "hovedprogram" f.eks. # a = 10

Først defineres funksjonen minFunksjon, som ikke skal ta imot noen parametere. Deretter defineres
prosedyren hovedprogram, som heller ikke tar noen parametre. Deretter kalles
hovedprogram. I hovedprogram oppretes variabel a = 42. Deretter oppretes variabel b = 0 og printes b.
Vi setter var b = a, fra naa har de samme verdien. Etterpaa settes a lik minFunksjon.
Vi kaller minFunksjon. I minFunksjon har vi for-løkke med indeks = x som skal kjøres to ganger (fordi in range(2) kaller løkkeoperasjoner to ganger).
I for-løkke oppretes og printes ut variabel c = 2, etterpaa blir c = 3 (c+=1), settes b=10.
Programmet slutter å funke på neste steg og gir feilmeldning fordi variabel a ble diffenert kun inne hovedprogram (dvs. den er lokalt)
, men vi trenger at a er globalt eller lokalt i minFunksjon. Hvis a ble diffenert fra før, skulle b += a og printes b. Funksjonen returnere verdi til b.


"""
def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)
# a = 10
def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print (b)
    print (a)
hovedprogram()
