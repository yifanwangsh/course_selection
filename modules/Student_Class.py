from modules import Person_Class

Person = Person_Class.Person

class Student(Person):
    def __init__ (self, name, role):
        Person.__init__(self, name, role)
        self.__courses = []

    