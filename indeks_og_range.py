"""
indeks kommand til str
"""
land = "NORGE"
for indeks in range( len(land) ):
    print( "Gi meg en " + land[indeks] )

"""
indeks til list
"""

taxi_kostnader = [145, 220, 91, 340]
for indeks in range( len(taxi_kostnader) ):
    if taxi_kostnader[indeks] <100:
        taxi_kostnader[indeks] = 100
print(taxi_kostnader)

"""
range til å oppgi kalkulasjon i bestemt område
"""

for tall in range(1,5):
    print(tall*tall)

"""
range til aa printe list av tall fra 0 til 4
"""

print( list(range(5)) )
