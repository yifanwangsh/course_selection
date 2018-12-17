import Person

class Teacher(Person.Person):
    def __init__(self, name, id, section_id,school_id):
        super().__init__(name, id)
        self.__section=section_id
        self.__school=school_id

    def listSections(self):
        return self.__section

    def updateGrade(self,section,student,grade):
        if section.getId() not in self.__section:
            raise KeyError("Rejected!")
            return 
        
        update_grade_sql="UPDATE public.student_grades SET grade = " + str(grade) + " WHERE student_id = " + str(student.getId()) + " AND section_id = " + str(section.getId())
        super().writeToDB(update_grade_sql)    

    def listStudentsName(self,section):
        if section.getId() not in self.__section:
            raise KeyError("Rejected!")
            return
        
        list_student_name_sql='''SELECT public.student_info.name FROM public.student_info LEFT JOIN public.section_info
            WHERE public.section_info.teacher_id = ''' + self.getId()
        data=super().readFromDB(list_student_name_sql)
        return data
        

    



        