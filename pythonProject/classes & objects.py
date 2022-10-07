from Student import Student    #von dem Student File die Student klasse importieren

student1 = Student("Jim", "Business", 3.1, False)   #student1 wird mit den Atributen aus der Klasse erstellt
student2 = Student("Kek", "Art", 4.1, True)

print(student2.on_honor_roll())
