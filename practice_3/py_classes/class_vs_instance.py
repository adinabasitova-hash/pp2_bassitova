# Here is class variable vs instance variable
class Student:
    school_name = "SITE"  # class variable, same for everyone

    def __init__(self, name):
        self.name = name  # instance variable, different per student

s1 = Student("Aida")
s2 = Student("Marat")
print(s1.school_name, s2.school_name)
print(s1.name, s2.name)