from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
from itertools import groupby
import operator

a= [1,2]
b= [3]
prod = product(a,b, repeat=2)                           # repeat legt die revisionen des Produktes fest
print(list(prod))                                       # Produkt aus beiden listen


a=[1,2,3]                                               # Wie oft kann etwas, mit allem mal genommen werden
perm = permutations(a, 2)
print(list(perm))

a=[1,2,3,4]                                             # alle möglichen Kombinationen | keine repetition (sind gegenseitig mal nehmen 2,2 / 3,3)
com = combinations(a, 2)
print(list(com))

a=[1,2,3,4]                                             # alle möglichen Kombinationen |  repetition (sind gegenseitig mal nehmen 2,2 / 3,3)
com = combinations_with_replacement (a, 2)
print(list(com))


a=[1,2,3,4]                                             # mit sich addieren -> 1,2,3,4 = 1+2 = 3 +3 =6 +4 = 10
acc = accumulate(a)
print(list(acc))

a=[1,2,3,4]                                             # mit sich multiplizieren
acc = accumulate(a, func=operator.mul)
print(list(acc))


def smaler_than_3(x):
    return x <3

a= [1,2,3,4]
group_obj = groupby(a, key=smaler_than_3)
for key, value in group_obj:
    print(key, list(value))
