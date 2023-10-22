#Punkt 1 og 2
liste = []
tall = -1
# liste.append(tall)
while tall != 0:
    # liste.append(tall)
    tall = int(input())
    liste.append(tall)
    if 0 in liste:
        liste.remove(tall)
    print(liste)

#Punkt 3

for tall in liste:
    print("Tall: " + str(tall))
#Punkt 4
minSum = 0
for tall in liste:
    if tall in liste:
        minSum += tall
print("Summen er " + str(minSum))
#Punkt 5
minste = 0
for tall in liste:
    liste.sort()

print("Minste: " + str(liste[0]))

største = liste[0]
for tall in liste:
    if tall > største:
        største = tall


print("Største: " + str(største))
    # if tall <  and tall != 0:
        # minste = tall
# print("Minste tall: " + str(minste))
