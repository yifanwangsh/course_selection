import Course
import Teacher
import uuid

Course = Course.Course
Teacher = Teacher.Teacher

class Section:
    def __init__(self):
        self.__id = self.gernerateId()

    @staticmethod
    def gernerateId():
        return uuid.uuid4()    