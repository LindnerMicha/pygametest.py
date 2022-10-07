mydict = {"name": "Max", "age":28, "city": "New York"}          # erstellen einer Vergleichstabelle
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

value = mydict["name"]                                          # ausgebabe eines Parameters
print(value)

mydict["email"] = "max@xyz.com"                                 # hinzufügen von parametern in die Tabelle
print(mydict)

del mydict["name"]                                              # entvernen bestimmter Parameter aus der Tabelle (alternativ .pop/.popitem)
print(mydict)

if "name" in mydict:                                            # prüfen ob sich element in der Liste befindet
    print(mydict["name"])
else:
    print("Steht hier nicht")

try:
    print(mydict["age"])
except:
    print("Error")

for key, value in mydict.items():                                 # einmal durch alle key argumente loopen + deren Wert anzeigen
    print(key, value)

mydict_cpy = mydict.copy()                                        # eine Tabelle kopieren ohne das die Main Liste verändert wird

my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)
value = my_dict[3]
print(value)
myTuple = (8, 7)
mydict = {myTuple: 15}
print(mydict)