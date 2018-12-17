import Person
import psycopg2

class Student(Person.Person):
    def __init__ (self, name, id, section_id, school_id):
        super().__init__(name, id)
        self.__section = section_id
        self.__school = school_id
    
    def enroll(self,section_id):
        if section_id in self.__section:
            print ("Already enrolled")
            return self.__section
        
        self.__section.append(section_id)
        return self.__section

    def paytuition():
        print ("Tuition paid!")