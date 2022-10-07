my_string = 'I\'m have a big cock'                          # ein String kann werden mit "" oder '' eingeleitet weden
print(my_string)                                            # mit """ """ kann ein String auf mehrere Zeilen formatiert werden
my_string = """i                                            
am having
a
big
cock"""
print(my_string)

myString = "hello world"                                    # auf einzelne Buchstaben in einem String zugreiffen
char = myString
print(char[2])


my_string = "hello world"                                   # auf einen definierten bereich des Strings zugreifen / ausschneiden
substring = my_string[1:5]
print(substring)

greeting = "hello"                                          # durch einen String schalten
for i in greeting:
    print(i)


myString = "      Hello World      "                        # entvernt unnötige Leerzeichen an anfang und ende
myString = my_string.strip()
print(myString)

print(myString.upper())                                     # Alles in Cpas setzen
print(myString.startswith("H"))                             # String anfang cecken -> Bool wert als ausgabe
print(myString.endswith("H"))                               # String Ende cecken -> Bool wert als ausgabe

print(myString.find("o"))                                   # sucht in meinem String den Index / stelle von o
print(myString.count("o"))                                  # zählt wie oft der Buchstabe 0 in dem String auftaucht

print(myString.replace("World", "Universe"))                # ersätzt World mit Universe

myString = "how are you doing"                              # String in Liste / Array konvertieren
myList = myString.split()
print(myList)
new_string = " ".join(myList)                               # Liste in String konvertieren ("...") gibt an was zwischen den Zeichen sein soll
print(new_string)


#!!!!!


my_list = ["a"]*6                                           # Array in String
my_string = "".join(my_list)
print(my_string)

#-------old style-------

var = "Tom"                                                 # %s (s = string )dient als Platzhalter
my_string = "the variable is %s" % var
print(my_string)
var = 3.14123
my_string = "the variable is %d" % var                      # %d (d = dezimal )dient als Platzhalter
print(my_string)
var = 3.14123
my_string = "the variable is %.2f" % var                     # %.2f (f = auf 2 float stellen)dient als Platzhalter
print(my_string)

#----------new style-------

var = 3.14123
var2 = 6
my_string = "the variable is {:.2f} and {}".format(var, var2)     # {} dient als Platzhalter, {:.2f} zwei stellen float variable
print(my_string)

#------- F-String newest style ---------

var = 3.14123
var2 = 6
my_string = f"the variable is {var} and {var2}"                    # f vor den "" zeigt einen F string an, in die {} können direkt die variablen geschrieben werden
print(my_string)