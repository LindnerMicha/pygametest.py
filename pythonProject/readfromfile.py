
mitarbeiter_file = open("mitarbeiter.txt", "r")     # Name in "" , Öffnungsart ("r" - read, "w" - write, "a" - append , "r+" - read & write)
print(mitarbeiter_file.readable())          # ist die Datei lesbar ?
#print(mitarbeiter_file.read())             # ganze Datei lesen
#print(mitarbeiter_file.readline())         # eine Zeile auslesen
#print(mitarbeiter_file.readline())         # die nächste Zeile auslesen
#print(mitarbeiter_file.readlines()[1])     # alle Zeilen in ein Array speichern und ausgeben [1] - Platz 1

for mitarbeiter in mitarbeiter_file.readlines():   # Array wird ausgegeben
    print(mitarbeiter)

mitarbeiter_file.close()                    # wieder schließen des Textes