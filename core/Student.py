import Person
import psycopg2
import Section

class Student(Person.Person):
    def __init__ (self, name, id):
        super().__init__(name, id)
    
    def enroll(self,section):
        if not isinstance(section,Section.Section):
            raise TypeError("Rejected")

        

    def paytuition(self,section):
        if not isinstance(section, Section.Section):
            raise TypeError("Rejected")
        
        print ("Tuition paid")