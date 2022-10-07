from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

a = "aaaaabbbbbbccccc"                                      # Zählt wie oft einzelne Komponenten in einem String verfügbar sind
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1)[0][0])                      # Zeigt die am meist vertretenes Element an [1][2][3] ->  meist, meist und zweot meist,...
print(list(my_counter.elements()))                          # String in eine Liste / array kompelieren


point = namedtuple("Point", "x,y")                          # Point anlegen mit deklaration x & y | den werten x & y werte zuweisen
pt = point(1,-4)
print(pt)


ordered_dict = OrderedDict()                                # Behält immer die hinzugefügte reihenfolge
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 9
ordered_dict["e"] = 1
print(ordered_dict)


d = defaultdict(int)                                        # besitzt einen key wenn dieser noch nicht festfgelegt ist
d["a"] = 1                                                  # wenn eine nicht belegte zahl aufgerufen wird, wird der standartwert für den jeweiligen Daentyp zurückgegeben zB int = 0, float = 0.0
d["b"] = 2
print(d["a"])


d = deque()
d.append(1)
d.append(2)
d.appendleft(3)                                             # Element wird linksbündig hinzugefügt -> deque([3, 1, 2])
print(d)

d.extend([4,5,6,7])                                         # Das deque wird um die Liste erweitert
print(d)

d.rotate(1)                                                 # Rotiert die reihenfolge (x) nach rechts
print(d)