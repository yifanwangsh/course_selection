import psycopg2
import Course
import School
import System

class Admin_system(System.System):
    def __init__(self):
        pass

    @classmethod
    def createTeacher(cls,name,password,school):
        if not isinstance(school, School.School):
            raise TypeError("Rejected")
        
        update_teacher_auth_info_sql="INSERT INTO teacher_auth_info(name,passcode) VALUES (\'" + name + "\',\'" + password + "\')"
        super().writeToDB(update_teacher_auth_info_sql)

        update_teacher_info_sql="INSERT INTO teacher_info(name,id,school_id) VALUES (\'" + name + "\',\'" + super().generateId() + "\',\'" + school.getId() + "\')"
        super().writeToDB(update_teacher_info_sql)

        print ("Teacher " + name + " has been created in " + school.getLocation() + "!\n")
    
    @classmethod
    def createCourse(cls,course_name,period,price):
        update_course_info_sql="INSERT INTO course_info(name,price,period) VALUES (\'" + course_name + "\'," + str(price) + "," + str(period) + ")"
        super().writeToDB(update_course_info_sql)

        print ("Course " + course_name + " has been created!\n")

    @classmethod
    def createSchool(cls,location):
        update_school_info_sql="INSERT INTO school_info(id,location) VALUES (\'" + super().generateId() + "\',\'" + location + "\')"
        super().writeToDB(update_school_info_sql)

        print ("School in " + location + " has been created!\n")

    @classmethod
    def listSchool(cls):
        query_school_info_sql="SELECT * FROM school_info"
        raw = super().readFromDB(query_school_info_sql)

        data={}
        for d in raw:
            data[d[1]]=School.School(d[0],d[1])
        return data

    @classmethod
    def listCourse(cls):
        query_course_info_sql="SELECT * FROM course_info"
        raw = super().readFromDB(query_course_info_sql)

        data={}
        for d in raw:
            data[d[0]]=Course.Course(d[0],d[1],d[2])
        return data
