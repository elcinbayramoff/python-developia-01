class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

student1 = Student("Resad", 14)
student2 = Student("Nicat", 14)

student1.display_info()  
student2.display_info()  
