myset = {1, 2, 3}                                   # Sets erlauben keine Kopien / Duplikate , nicht geordnet
print(myset)

myset = set("Hello")                                # Gibt alle elemente im Set wieder, geordnet & einzeln

myset.add(1)                                        # Element hinzufügen
myset.add(2)
myset.add(3)
myset.remove(3)

#myset.clear()                                       # gesammtes Set löschen

for i in myset:                                      # durch das Set schalten
    print(i)

if "l" in myset:                                     # Set auf inhalt durchsuchen
    print("Yo, steht hier")
else:
    print("Nö, steht hier net")

print(myset)

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
u = odds.union(evens)                                # Legt die beiden Sets zusammen
print(u)
i = odds.intersection(evens)                         # Vergleicht die beiden Sets und stellt die gemeinsamen Zahlen da
print(i)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
diff = setA.difference(setB)                          # gibt die Unterschiede zwischen SetA & SetB aus
print(diff)
diff = setA.symmetric_difference(setB)                # gibt aus was dem jeweils anderem Set an werten fehlt
print(diff)
setA.update(setB)                                     # Addiert die beiden sets, da es aber keine duplikate gibt
print(setA)

setA.intersection_update(setB)                        # Addiert die beiden sets, behält aber nur Zahlen die in beiden Sets vorhanden sind
print(setA)
setA.difference_update(setB)                          # Addiert die beiden sets, löscht aber Zahlen die in beiden Sets vorhanden sind
print(setA)
setA.symmetric_difference_update(setB)                # Addiert die beiden sets, behält alle zahlen aus SetA und SetB. Gibt es sie aber in beiden werden sie gelöscht
print(setA)

a = frozenset([1,2,3,4])                              # kann nach dem Erstellen nichtmehr verändert werden
print(a)