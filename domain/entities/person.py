
class Person:
    def _init_(self , name:str , age:int):
        self.name= name
        self.age=age

    def getName(self):
        return self.name
    def setName(self, name:str):
        self.name= name