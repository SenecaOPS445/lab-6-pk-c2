#!/usr/bin/env python3

from student import Student

if __name__ == '__main__':
    # Create the first student object and add grades for each class
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops235', 2.0)
    student1.addGrade('ops435', 3.0)

    # Create the second student object and add grades for each class
    student2 = Student('Jessica', 123456)
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display information for the student1 object
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for the student2 object
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())

    # Additional tests
    student3 = Student('Jack', 931686102)
    student3.addGrade('ops535', 2.0)
    student3.addGrade('win310', 0.0)
    print(student3.displayStudent())
    print(student3.displayGPA())
    print(student3.displayCourses())

    student4 = Student('Jen', 987654321)
    print(student4.displayStudent())
    print(student4.displayGPA())
    print(student4.displayCourses())
