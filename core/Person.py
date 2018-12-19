import System

class Person(System.System):
    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def getName(self):
        return self.__name

    def getId(self):
        return self.__id