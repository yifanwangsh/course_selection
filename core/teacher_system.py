import System
import Teacher
class Teacher_system(System.System):
    def __init__():
        pass
    
    @classmethod
    def login(username,password):
        auth_query_sql="SELECT username,password FROM public.teacher_auth_info"
        auth=super().readFromDB(auth_query_sql)

        for d in auth:
            if username==d[0] and password==d[1]:
                print ("Login Successful!")
                teacher_info_sql="SELECT * FROM public.teacher_info WHERE name = \'" + username + "\'"
                info=super().readFromDB(teacher_info_sql)[0]
                return Teacher.Teacher(info[0],info[1],info[2],info[3])
        print ("Login Failed")
        return