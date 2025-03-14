#!/usr/bin/env python3

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Convert number to string
        self.courses = {}

    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    def addGrade(self, course, grade):
        self.courses[course] = grade

    def displayGPA(self):
        if not self.courses:  # Handle division by zero
            return 'GPA of student ' + self.name + ' is 0.0'
        gpa = sum(self.courses.values()) / len(self.courses)
        return 'GPA of student ' + self.name + ' is ' + str(gpa)

    def displayCourses(self):
        passed_courses = [course for course, grade in self.courses.items() if grade != 0.0]
        return passed_courses
