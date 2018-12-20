import System
import Teacher

class Teacher_system(System.System):
    def __init__(self):
        pass
    
    @classmethod
    def login(cls,name,passcode):
        query_teacher_auth_sql="SELECT 1 FROM teacher_auth_info WHERE name = \'" + name + "\' AND passcode = \'" + passcode + "\' LIMIT 1"
        if super().readFromDB(query_teacher_auth_sql):
            teacher_info_sql="SELECT * FROM teacher_info WHERE name = \'" + name + "\'"
            raw=super().readFromDB(teacher_info_sql)[0]
            print ("Login Successful!\n")
            return Teacher.Teacher(raw[0],raw[1])
        else:
            print ("Login Failed!\n")
            return