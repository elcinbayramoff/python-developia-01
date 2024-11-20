# class Student:
#     def __init__(self, name, surname, classes, age):
#         self.name = name
#         self.surname = surname
#         self.classes = classes
#         self.age = age

#     def ShowInformation(self):
#         return f"Name: {self.name}, Surname: {self.surname}, Class: {self.classes}, Age: {self.age}"

# class School(Student):
#     def __init__(self, name, surname, classes, age, school_name):
#         Student.__init__(self, name, surname, classes, age)
#         self.school_name = school_name



# student1 = Student("Ali", "Hesenov", "9B", 15, "Baku international school")
# student2 = Student("Aysel", "Kerimova", "11C", 17, "Baku international school")

# print(student1.ShowInformation())
# print(student2.ShowInformation())

#////////////////////////////////////////////////////////////////////////////////////////////////////////

# class School:
#     def __init__(self, school_name, address):
#         self.school_name = school_name
#         self.address = address

#     def __str__(self):
#         return f"School: {self.school_name}, Address: {self.address}"
    
# class Student:
#     def __init__(self, name, surname, classes, age, school):
#         self.name = name
#         self.surname = surname
#         self.classes = classes
#         self.age = age
#         self.school = school

#     def ShowInformation(self):
#         return (f"Name: {self.name}, Surname: {self.surname}, Class: {self.classes}, Age: {self.age}, "
#                 f"{self.school}")

#     def get_school_name(self):
#         school = self.school
#         return school.school_name
    
# school1 = School("Baku International School", "Baku, Azerbaijan")
# school2 = School("Azerbaijan Technical School", "Ganja, Azerbaijan")

# student1 = Student("Ali", "Hesenov", "9B", 15, school1)
# student2 = Student("Aysel", "Kerimova", "11C", 17, school2)

# print(student1.ShowInformation())
# print(student2.ShowInformation())

# print(student1.get_school_name())