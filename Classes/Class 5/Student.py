from functools import cmp_to_key

class Student:
    def __init__(self, name, student_id, cgpa, age):
        self.name = name
        self.student_id = student_id
        self.cgpa = cgpa
        self.age = age
    
    def __str__(self):
        return f"Name: {self.name} ID: {self.student_id} CGPA: {self.cgpa}"
    

def my_comparator(a, b):
    if a.cgpa > b.cgpa:
        return -1
    elif a.cgpa < b.cgpa:
        return 1
    else:
        if a.student_id < b.student_id:
            return -1
        elif a.student_id > b.student_id:
            return 1
        else:
            return 0
    

students = [Student("A", 1, 3.97, 25), Student("B", 2, 4.00, 27), Student("C", 3, 4.00, 26), Student("D", 4, 3.98, 26)]
students.sort(key=cmp_to_key(my_comparator))

for student in students:
    print(student)
