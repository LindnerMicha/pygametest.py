
try:
    test = 10/0
    number = int(input("Enter a Number: "))
    print(number)

except ZeroDivisionError as err:   #immer die genauen fehler angeben !
    print(err)
except ValueError:
    print("Invalid Input")