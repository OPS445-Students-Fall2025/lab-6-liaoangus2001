#!/usr/bin/env python3
# Author ID: lliao16

class Student:
    # Define the name and number when a student object is created, ex. student1 = Student('john', 025969102)
    def __init__(self, name, number):
        self.name = str(name)
        self.number = str(number)   # 關鍵修正：學號一律轉字串
        self.courses = {}

    # Return student name and number
    def displayStudent(self):
        return 'Student Name: ' + str(self.name) + '\n' + 'Student Number: ' + str(self.number)

    # Add a new course and grade to students record
    def addGrade(self, course, grade):
        try:
            g = float(grade)
        except (TypeError, ValueError):
            g = 0.0
        self.courses[str(course)] = g

    # Calculate the grade point average of all courses and return a string
    def displayGPA(self):
        if len(self.courses) == 0:
            gpa_value = 0.0            # 避免 ZeroDivisionError，符合題目範例
        else:
            total = 0.0
            for course in self.courses.keys():
                total += self.courses[course]
            gpa_value = total / len(self.courses)
        return 'GPA of student ' + self.name + ' is ' + str(gpa_value)

    # Return a list of course that the student passed (not a 0.0 grade)
    def displayCourses(self):
        return [c for c, g in self.courses.items() if g > 0.0]

if __name__ == '__main__':
    # Create first student object and add grades for each class
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades for each class
    student2 = Student('Jessica', 123456)  # 測試整數學號
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display information for student1 object
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for student2 object
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
