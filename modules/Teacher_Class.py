from modules import Person_Class

Person = Person_Class.Person

class Teacher(Person):
    def __init__(self, name, role):
        Person.__init__(self, name, role)
        

    



        