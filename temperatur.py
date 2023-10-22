#Punkt 1

fil1 = open("max_temperatures_per_month.csv")
ordbok_month = {}
def max_temp_ordbok(fil1):
    for linje in fil1:
        biter = linje.split(",")
        dag = biter[0]
        # print(dag)
        temp1 = float(biter[1])
        ordbok_month[dag] = temp1

    # print(ordbok_month)
    return ordbok_month,
max_temp_ordbok(fil1)
# print(ordbok_month)

# Punkt 2 og 3

fil2 = open("max_daily_temperature_2018.csv")
def temperatur_hoyere_enn_per_month(ordbok_month, fil2):

    for linjee in fil2:
        bitter = linjee.split(",")

        # print(bitter)
        mnd = bitter[0]
        # print(dagg)
        dag = bitter[1]
        tempo = float(bitter[2])
        if ordbok_month[mnd] < tempo:

            print("Ny varmerekord paa "+ dag + " " + mnd + ": " + str(tempo) + " Celcius"  )
            ordbok_month[mnd] = tempo
            #Punkt 3
    return ordbok_month

temperatur_hoyere_enn_per_month(ordbok_month,fil2)
print(ordbok_month)
