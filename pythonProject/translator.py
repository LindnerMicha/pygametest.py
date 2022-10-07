def translate(satz):
    translation = ""
    for letter in satz:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation +"g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a Translation: ")))
