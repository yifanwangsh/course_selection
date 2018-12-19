import Person

class Teacher(Person.Person):
    def __init__(self, id, name, school_id):
        super().__init__(name, id)
        self.__school=school_id

    def listSections(self):
        query_section_sql="SELECT id FROM section_info WHERE teacher_id=\'" + self.getId() + "\'"
        data=super().readFromDB(query_section_sql)[0]
        return data

    def updateGrade(self,section,student,grade):
        if section.getId() not in self.listSections():
            raise KeyError("Rejected!") 
        
        update_grade_sql="UPDATE student_grades SET grade = " + str(grade) + " WHERE student_id = \'" + student.getId() + "\' AND section_id = \'" + section.getId() + "\'"
        super().writeToDB(update_grade_sql)    

    def listStudentsName(self,section):
        if section.getId() not in self.listSections():
            raise KeyError("Rejected!")
        
        list_student_name_sql='''SELECT student_info.name FROM student_info LEFT JOIN section_info
            WHERE section_info.teacher_id = ''' + self.getId()
        data=super().readFromDB(list_student_name_sql)
        return data