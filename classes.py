class Student:
    def __init__(self,name,std):
        self.name =name
        self.std = std

    def display(self):
        print("Name is ",self.name)
        print("Std is ",self.std)

s=Student("Joseph",12)
s.display()

