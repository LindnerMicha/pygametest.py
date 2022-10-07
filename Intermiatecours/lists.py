mylist = ["banana", "cerry", "apple"]
print(mylist)

print(len(mylist))

mylist.append("Lemon") # an liste anhängen
print(mylist)

mylist.insert(1, "Blueberry") # an stelle 1 einfügen
print(mylist)

item = mylist.pop() # letzte nehemen und entvernen
print(item)
print(mylist)

item = mylist.remove("cerry") #cerry aus der Liste entvernen
print(mylist)

item = mylist.sort() #liste sortieren
print(mylist)

item = mylist.reverse() #reiehenfolge der elemente umkehren
print(mylist)

new_list = sorted(mylist) #eine neue Liste wird erstellet, mit den neu Sortierten elementen der alten angegebene Liste

multiList = [0]*5 # erstellt eine Liste mit 5 mal dem in [] angegebenen Wert

mylist2 = [1, 2, 3, 4, 5]       #addieren / anhängen der beiden listen
new_list2 = mylist + mylist2
print(new_list2)

varList = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # erstellt eine neue Liste mit den werten der angegebene in bestimmten Grenzbereichen
a = varList[1:5]  # ::2 von beginn wird jedes zweite Item herausgenommen
print(a)

list_org = ["Banana", "Apple", "Lemon"]
list_cpy = list_org                     # wenn die Kopie bearbeitet wird, wird die Orginale Liste auch verändert !!
list_cpy = list_org.copy()              # der richtige weg Listen zu kopieren ohne das Orginal zu verändern
list_cpy.append("Kelp")

b = [1, 2, 3, 4, 5, 6]                  # eine weitere Liste mit x10 zahlen
c = [i*i for i in a]
print(b)
print(c)