from modules import Course_Class
from modules import Teacher_Class
import uuid

Course = Course_Class.Course
Teacher = Teacher_Class.Teacher

class Section:
    def __init__(self):
        self.__id = self.gernerateId()

    @staticmethod
    def gernerateId():
        return uuid.uuid4()    