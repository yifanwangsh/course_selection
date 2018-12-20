import psycopg2
import Student
import Section
import School
import System

class Student_system(System.System):
    def __init__(self):
        pass

    @classmethod
    def login(cls,name,passcode):
        query_student_auth_sql="SELECT 1 FROM student_auth_info WHERE name = \'" + name + "\' AND passcode = \'" + passcode + "\' LIMIT 1"
        if super().readFromDB(query_student_auth_sql):
            student_info_sql="SELECT * FROM student_info WHERE name = \'" + name + "\'"
            raw=super().readFromDB(student_info_sql)[0]
            print ("Login Successful!\n")
            return Student.Student(raw[1],raw[0])
        else:
            print ("Login Failed!\n")
            return

    @classmethod
    def signup(cls,name,password,school):
        if not password or not name:
            raise KeyError("username or password cannot be null")
        
        if not isinstance(school, School.School):
            raise TypeError("Rejected")
        
        update_auth_sql="INSERT INTO student_auth_info(name,passcode) VALUES (\'" + name + "\',\'" + password + "\')"
        super().writeToDB(update_auth_sql)

        update_student_info="INSERT INTO student_info(name,id,school_id) VALUES (\'" + name + "\',\'" + super().generateId() + "\',\'" + str(school.getId()) + "\')"
        super().writeToDB(update_student_info)

        print ("You've signed up successfully as " + name + "!\n")
    
    @classmethod
    def listAvailableSections(cls,student):
        if not isinstance(student,Student.Student):
            raise TypeError("Rejected")
        
        query_available_section_sql="SELECT sec.id,sec.course_name,sch.location,sec.section_id FROM section_info AS sec LEFT JOIN student_info AS stu ON sec.school_id=stu.school_id LEFT JOIN school_info AS sch ON sec.school_id=sch.id"
        raw=super().readFromDB(query_available_section_sql)

        data={}
        for d in raw:
            section_description=d[1] + " in " + d[2] + " section number " + str(d[3])
            data[section_description] = Section.Section(d[0])
        return data
    