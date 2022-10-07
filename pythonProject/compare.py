monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April"
}

i = 0;

while True:
    invar = input("Sag mir was: ")

    if invar == "break":
        break

    conv = (monthConversion.get(invar, "Not a valit Key"))
    count = int(input("Wie oft soll ichs dir sagen ? : "))
    while i < count:
        print("Die Übersetzung lautet: " + conv)
        i +=1
