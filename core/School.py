import Course
import Teacher
import System

class School(System.System):
    def __init__ (self, id, location):
        self.__location = location
        self.__id = id

    def setLocation(self, location):
        self.__location = location

    def getLocation(self):
        return self.__location    

    def getId(self):
        return self.__id

    def createSection(self,course,teacher):
        if not isinstance(course,Course.Course) or not isinstance(teacher,Teacher.Teacher):
            raise TypeError("Rejected!")
        
        query_max_section_id_sql="SELECT MAX(section_id) FROM section_info WHERE course_name=\'" + course.getName() + "\' AND teacher_id=\'" + teacher.getId() + "\' AND school_id=\'" + self.getId() + "\'"
        section_id = super().readFromDB(query_max_section_id_sql)[0][0]+1

        create_section_table_sql="CREATE TABLE " + course.getName() + "_in_" + self.getLocation() + "_" + str(section_id) + " (student_id varchar NOT NULL PRIMARY KEY, student_grade integer, tuition_paid boolean DEFAULT FALSE)"
        super().writeToDB(create_section_table_sql)

        update_section_info_sql="INSERT INTO section_info (id,course_name,school_id,teacher_id,section_id) VALUES (\'" + super().generateId() + "\',\'" + course.getName() + "\',\'" + self.getId() + "\',\'" + teacher.getId() + "\'," + str(section_id) +")"
        super().writeToDB(update_section_info_sql)
    
    def listTeacher(self):
        query_teacher_info_sql="SELECT * FROM teacher_info WHERE school_id= \'" + self.getId() + "\'"
        raw = super().readFromDB(query_teacher_info_sql)

        data={}
        for d in raw:
            data[d[1]]=Teacher.Teacher(d[0],d[1])
        return data