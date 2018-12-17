import psycopg2
import uuid
import Student
import System

Student=Student.Student

class Student_system(System.System):
    def __init__(self):
        pass

    @classmethod
    def login(cls,username,password):
        
        auth_query_sql="SELECT username,password FROM public.student_auth_info"
        auth=super().readFromDB(auth_query_sql)

        for d in auth:
            if username==d[0] and password==d[1]:
                print ("Login Successful!")
                student_info_sql="SELECT * FROM public.student_info WHERE name = \'" + username + "\'"
                info=super().readFromDB(student_info_sql)[0]
                return Student(info[0],info[1],info[2],info[3])
        print ("Login Failed")
        return

    @classmethod
    def signup(cls,username,password):
        if not password or not username:
            raise KeyError("username or password cannot be null")
        
        update_auth_sql="INSERT INTO public.student_auth_info(username,password) VALUES (\'" + username + "\',\'" + password + "\')"
        super().writeToDB(update_auth_sql)

        random_id=uuid.uuid4().int>>100
        update_student_info="INSERT INTO public.student_info(name,id) VALUES (\'" + username + "\'," + str(random_id) + ")"
        super().writeToDB(update_student_info)

    @classmethod
    def enroll(cls,student, section_id):
        if not isinstance (student,Student):
            raise TypeError("Rejected")
            return
        sections=student.enroll(section_id)

        section_str=str(sections).replace("[","{").replace("]","}")
        update_student_info_sql="UPDATE public.student_info SET section_id = \'" + section_str + "\' WHERE name = \'" + student.getName() + "\'"
        super().writeTODB(update_student_info_sql)

s=Student_system()
s.login("user2","user2")
