import Person
import Section
import Student

class Teacher(Person.Person):
    def __init__(self, id, name):
        super().__init__(name, id)

    def listSections(self):
        query_section_sql="SELECT id FROM section_info WHERE teacher_id=\'" + self.getId() + "\'"
        raw=super().readFromDB(query_section_sql)
        data=[]
        for d in raw:
            data.append(d[0])
        return data

    def updateGrade(self,section,student,grade):
        if not isinstance(section,Section.Section) or not isinstance(student,Student.Student):
            raise TypeError("Rejected")

        if section.getId() not in self.listSections():
            raise KeyError("Rejected!") 
        
        query_section_info_sql='''SELECT sec.course_name,sch.location,sec.section_id FROM section_info AS sec LEFT JOIN school_info AS sch ON sec.school_id=sch.id
                                    WHERE sec.id=\'''' + section.getId() + "\'"
        raw=super().readFromDB(query_section_info_sql)[0]
        table_name=raw[0]+"_in_"+raw[1]+"_"+str(raw[2])

        update_grade_sql="UPDATE " + table_name + " SET student_grade = " + str(grade) + " WHERE student_id = \'" + student.getId() + "\'"
        super().writeToDB(update_grade_sql)    

    def listStudentsName(self,section):
        if section.getId() not in self.listSections():
            raise KeyError("Rejected!")
        
        query_section_info_sql='''SELECT sec.course_name,sch.location,sec.section_id FROM section_info AS sec LEFT JOIN school_info AS sch ON sec.school_id=sch.id
                                    WHERE sec.id=\'''' + section.getId() + "\'"
        raw=super().readFromDB(query_section_info_sql)[0]
        table_name=raw[0]+"_in_"+raw[1]+"_"+str(raw[2])

        query_student_name_sql="SELECT stu.name FROM student_info AS stu LEFT JOIN " + table_name + " AS sec ON sec.student_id=stu.id"
        raw=super().readFromDB(query_student_name_sql)

        data=[]
        for d in raw:
            data.append(d[0])
        return data