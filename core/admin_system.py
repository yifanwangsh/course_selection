import psycopg2
import uuid
import System

class Admin_system(System.System):
    sectionId_generator=(i for i in range(1,100))
    
    def __init__(self):
        pass

    @classmethod
    def createTeacher(cls,name,password,school_id):
        update_teacher_auth_info_sql="INSERT INTO public.teacher_auth_info(username,password) VALUES (\'" + name + "\',\'" + password + "\')"
        super().writeToDB(update_teacher_auth_info_sql)

        random_id=uuid.uuid4().int>>100
        update_teacher_info_sql="INSERT INTO public.teacher_info(name,id,school_id) VALUES (\'" + name + "\'," + str(random_id) + "," + str(school_id) + ")"
        super().writeToDB(update_teacher_info_sql)
    
    @classmethod
    def createSection(cls,course,school_id):
        section_id=next(cls.sectionId_generator)
        update_section_info_sql="INSERT INTO public.section_info(id,school_id,course) VALUES (" + str(section_id) + "," + str(school_id) + ",\'" + course + "\')"
        super().writeToDB(update_section_info_sql)
    
    @classmethod
    def createCourse(cls,course_name,period,price):
        update_course_info_sql="INSERT INTO public.course_info(course_name,price,period) VALUES (\'" + course_name + "\'," + str(price) + "," + str(period) + ")"
        super().writeToDB(update_course_info_sql)
