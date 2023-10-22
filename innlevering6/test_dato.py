#Punkt 2
from dato import Dato
def hovedprogram():

    test = Dato(15,2,2)
    print("Her er datoens aar i utgangspunkt:", test.hent_aar())
    dato = test.hent_str_dato()
    dag = dato[0]
    maaned = dato[1]
    aar = dato[2]
    a = dag + maaned + aar
    print(a)
    print("Her er datoen: ", dag, maaned, aar)
    # print(test.hent_str_dato())
    test.sjek()



hovedprogram()
