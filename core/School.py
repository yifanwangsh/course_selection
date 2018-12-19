import Course
import Teacher
import System

class School(System.System):
    def __init__ (self, id, location):
        self.__location = location
        self.__id = id
        self.__generator = (i for i in range(1,100))

    def setLocation(self, location):
        self.__location = location

    def getLocation(self):
        return self.__location    

    def getId(self):
        return self.__id

    def createSection(self,course,teacher):
        if not isinstance(course,Course.Course) or not isinstance(teacher,Teacher.Teacher):
            raise TypeError("Rejected!")
        
        section_id=next(self.__generator)

        create_section_table_sql="CREATE TABLE " + course.getName() + "_in_" + self.getLocation() + "_" + str(section_id) + " (student_id varchar NOT NULL PRIMARY KEY, student_grade integer, tuition_paid boolean DEFAULT FALSE)"
        super().writeToDB(create_section_table_sql)

        update_section_info_sql="INSERT INTO section_info (id,course_name,school_id,teacher_id,section_id) VALUES (\'" + super().generateId() + "\',\'" + course.getName() + "\',\'" + self.getId() + "\',\'" + teacher.getId() + "\'," + str(section_id) +")"
        super().writeToDB(update_section_info_sql)

# s=School("schoolid","Shanghai")
# c=Course.Course("python",123,456)
# t=Teacher.Teacher("teacher_id","yifan")
# s.createSection(c,t)