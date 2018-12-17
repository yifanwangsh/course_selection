import uuid
import Course
import School

School = School.School
Course = Course.Course

class Person:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def getName(self):
        return self.__name

    def getId(self):
        return self.__id