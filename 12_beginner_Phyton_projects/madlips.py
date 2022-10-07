
text= ["The sky is (a) ", "The gras is (b)", "I love (c)\n"]

for i in text:
    k = text.index(i)
    print(text[k])

a = input("Eingabe (a) ")
b = input("Eingabe (b) ")
c = input("Eingabe (c) ")

print("\nDein Ergebnis lautet: ")
text= ["\nThe sky is ", "The gras is ", "I love "]

for i in text:
    k = text.index(i)
    if k == 0:
        print(text[k] + a)
    elif k == 1:
        print(text[k] + b)
    elif k == 2:
        print(text[k] + c)