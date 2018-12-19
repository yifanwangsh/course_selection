import psycopg2
import Student
import Section
import School
import System

class Student_system(System.System):
    def __init__(self):
        pass

    @classmethod
    def login(cls,username,password):
        
        auth_query_sql="SELECT name,passcode FROM student_auth_info"
        auth=super().readFromDB(auth_query_sql)

        for d in auth:
            if username==d[0] and password==d[1]:
                print ("Login Successful!")
                student_info_sql="SELECT * FROM student_info WHERE name = \'" + username + "\'"
                info=super().readFromDB(student_info_sql)[0]
                return Student.Student(info[0],info[1])
        print ("Login Failed")
        return

    @classmethod
    def signup(cls,username,password,school):
        if not password or not username:
            raise KeyError("username or password cannot be null")
        
        if not isinstance(school, School.School):
            raise TypeError("Rejected")
        
        update_auth_sql="INSERT INTO student_auth_info(name,passcode) VALUES (\'" + username + "\',\'" + password + "\')"
        super().writeToDB(update_auth_sql)

        update_student_info="INSERT INTO student_info(name,id,school_id) VALUES (\'" + username + "\',\'" + super().generateId() + "\',\'" + str(school.getId()) + "\')"
        super().writeToDB(update_student_info)