import uuid

class Section:
    def __init__(self):
        self.__id = self.gernerateId()

    @staticmethod
    def gernerateId():
        return uuid.uuid4()

    def getId():
        return self.__id 