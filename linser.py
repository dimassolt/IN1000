from random import randrange
antall_trekk = 0
score = 0
while antall_trekk < 100000:
    antall_trekk += 1
    venstre = randrange(4)
    hoyere = randrange(3)
    if venstre!= hoyere and (venstre == 1 or venstre == 2) and (hoyere == 3 or hoyere == 4):
        score += 1
print(score/antall_trekk)
