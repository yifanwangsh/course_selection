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
        
        update_student_grades_info="INSERT INTO public.student_grades(student_id,section_id) VALUES (" + str(self.getId()) + "," + str(self.getId()) + ")"
        super().writeToDB(update_student_grades_info)

    def paytuition():
        print ("Tuition paid!")