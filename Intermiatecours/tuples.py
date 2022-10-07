myTuple = ("Max", 28, "Boston")                                #  Nicht veränderbare Variable / Tuple erstellen
myTuple = tuple(["Max", 28, "Boston"])
print(myTuple)

item = myTuple[2]                                              # Auslesen des Tuple bzw eines Items darin
print(item)

for i in myTuple:                                              # Auslesen aller Elemente
    print(i)

if "Max" in myTuple:                                           # Befindet sich etwas in meinem Tuple ?
    print("Yes")
else:
    print("No")

myTuple2 = ('a','p','p','l','e')
print(len(myTuple2))                                           # länge meines Tuple
print(myTuple2.count('p'))                                     # wie oft ist etwas in meienm Tuple ?

myList = list(myTuple2)                                        # Eine Liste in ein Tupel formatieren
myTuple2 = tuple(myList)                                       # Ein Tuple in eine Liste formatieren

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)                                # slice / teilen eines Tupels ziwschen bestimmten Grenzwerten
b = a[2:5]
print(b)

myTuple = ("Max", 28, "Boston")                                # Tuple auspacken in variablen
name, age, city = myTuple
print(name)
print(age)
print(city)


myTuple = (1, 2, 3, 4)                                         # entpacken in eine variable, einen zwischenbereich, und die letzte variable
i1, *i2, i3 = myTuple
print(i1)
print(i2)
print(i3)


import sys                                                      # Tuples verbraucht weniger Speicher und ist effizienter
my_list = [0, 1, 2, "hello", True]
myTuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(myTuple), "bytes")