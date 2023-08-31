import uuid

"""ITF 08 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name :
Delivery Date :
"""
Name = input('Enter your name :')
Delivery_Date = 30 / 8 / 2023


# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark (user_input)


class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()
        self.course_name = course_name
        self.course_mark = course_mark


class Student:
    # TODO 3 define static variable indicates total student count
    total_student = 0

    # TODO 4 define a constructor which includes
    # student_id (unique using uuid module)
    # student_name (user input)
    # student_age (user input)
    # student_number (user_input)
    # courses_list (List of Course Objects)

    def __init__(self, student_name, student_age, student_number, courses_list=[]):
        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = courses_list
        Student.total_student += 1

    # TODO 5 define a method to enroll new course to student courses list
    def enroll_course(self, courses_list):
        self.courses_list.append(courses_list)
        print(f"Enrolled in {courses_list} successfully!")

    # method to get_student_details as dict
    def get_student_details(self):
        return {
            'student_id': self.student_id,
            'student_name': self.student_name,
            'student_age': self.student_age,
            'student_number': self.student_number,
            'courses_list': self.courses_list
        }

    # method to get_student_courses
    def get_student_courses(self):
            # TODO 6 print student courses with their marks
            print("Courses with marks:")
            for course in self.courses_list:
                print(f"Course: {course['name']}, Mark: {course['mark']}")

    # method to get student_average as a value
    def get_student_average(self):
        # TODO 7 return the student average
        marks = [course['mark'] for course in self.courses_list if 'mark' in course]
        if marks:
            return sum(marks) / len(marks)
        else:
            return None


# in Global Scope
# TODO 8 declare empty students list
students = []
while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit\n"
                              "Choice: "))
        if 1 <= selection <= 6:
            if selection == 1:
                student_number = input("Enter Student Number")
                student_name = input("Enter Student Name")
                if student_number in students:
                    print("Student number already exists. Please enter a different number.")
                while True:
                    try:
                        student_age = int(input("Enter Student Age"))
                        break
                    except:
                        print("Invalid Value")
                # TODO 11 create student object and append it to students list
                student = Student(student_number, student_name, student_age)
                students.append(student)
                print("Student added successfully!")
            elif selection == 2:
                def find_student_index_by_number(number):
                    for index, student in enumerate(students):
                        if student_number == number:
                            return index
                    return -1


                student_number = input("Enter Student Number")
                student_index = find_student_index_by_number(student_number)

                if student_index != -1:
                    del students[student_index]
                    print("Student Deleted Successfully")
                else:
                    print("Student Not Exist")
            elif selection == 3:
                student_number = input("Enter Student Number")
                # TODO 13 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")
                student_found = False
                for student in students:
                    for student in students:
                        if student_number == student_number:
                            print("Student Details:")
                            print(f"Number: {student_number}")
                            print(f"Name: {student_name}")
                            print(f"Age: {student_age}")
                            student_found = True
                            break

                if not student_found:
                    print("Student Not Exist")
            elif selection == 4:
                student_number = input("Enter Student Number: ")
                target_student = next((student for student in students if student_number == student_number),
                                      None)
                if target_student:
                    average = target_student.get_student_average()
                    print(f"Student Average: {average}")
                else:
                    print("Student Not Exist")
            elif selection == 5:
                def find_student_index_by_number(number):
                    for index, student in enumerate(students):
                        if student_number == number:
                            return index
                    return -1


                student_number = input("Enter Student Number: ")
                student_index = find_student_index_by_number(student_number)
                if student_index != -1:
                    course_name = input("Enter Course Name: ")
                    course_mark = float(input("Enter Course Mark: "))

                    course = {"name": course_name, "mark": course_mark}
                    students[student_index].courses_list.append(course)  # Corrected line
                    print("Course Added Successfully")
                else:
                    print("Student Not Exist")
            elif selection == 6:
                print("Exiting the program...")
                exit()
        else:
            print("Invalid choice. Please enter a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number.")
