import Student
import Student_system
import Teacher_system
import Admin_system
import School
import util

def student_system():
    system=Student_system.Student_system
    while True:
        print ('''---You are now in student system---
    1.Log in
    2.Sign up
    q.Exit to main menu
        
How can I help you?''')
        c=input("==>")
        if c=="q": break
        
        elif c=="1":
            print ("Please enter your name")
            name=input("==>")
            print ("Please enter your password")
            password=input("==>").strip()
            s=system.login(name,password)
            if s:
                student_loged_in(s)
        
        elif c=="2":
            print ("Please enter your name")
            name=input("==>")
            print ("Please enter a password for authorization")
            passcode=input("==>")
            school=util.chooseSchool()
            if school:
                system.signup(name,passcode,school)
            
def student_loged_in(student):
    if not isinstance(student,Student.Student):
        raise TypeError("Rejected")
    
    system=Student_system.Student_system
    while True:
        print ("---You are now loged in as " + student.getName() + " ---")
        print ('''
    1.enroll in a section
    2.pay tuition for a section
    q.log out
        
How can I help you?''')
        c=input("==>")
        if c=="q":break

        elif c=="1":
            available_section_info=system.listAvailableSections(student)
            section=util._choose(available_section_info,"section")
            if section:
                student.enroll(section)
        
        elif c=="2":
            enrolled_section_info=student.listEnrolledSection()
            section=util._choose(enrolled_section_info,"section")
            if section:
                student.paytuition(section)

        else:
            print ("Invalid choice. Rejected")


def teacher_system():
    system=Teacher_system.Teacher_system
    print ("---You are now in Teacher system---")
    print ("Please enter your name")
    name=input("==>")
    print ("Please enter your password")
    passcode=input("==>")
    teacher=system.login(name,passcode)
    if teacher:
        while True:
            print ("---You are now logged in as " + teacher.getName() + " ---")
            print ('''
    1.upgrade student grade
    2.check students' name in a section
    3.check section
    q.log out

How can I help you?''')
            c=input("==>")
            if c=="q":break
            
            elif c=="1":
                print ("You are teaching the following sections:")
                section_info=teacher.listSections()
                section=util._choose(section_info,"section")
                if section:
                    print ("Please choose which student's grade to update:")
                    student=util._choose(teacher.listStudentsName(section),"student")
                    if student:
                        print ("Please enter his/her grade")
                        grade=input("==>")
                        teacher.updateGrade(section,student,grade)
            
            elif c=="2":
                print ("You are teaching the following sections:")
                section_info=teacher.listSections()
                section=util._choose(section_info,"section")
                if section:
                    print ("These students are in your section:")
                    util.listKeys(teacher.listStudentsName(section))

            elif c=="3":
                print ("You are teaching the following sections:")
                util.listKeys(teacher.listSections().keys())
                print ("-----------------\n")

def admin_system():
    print ("You need to provide admin credential to login")
    p=input("==>")
    if not p=="admin":
        print ("Credential is wrong!")
        return
    
    system=Admin_system.Admin_system()
    while True:
        print ('''---You are now in admin system---
    1.create a new school
    2.create a new course
    3.create a new teacher
    4.create a new section
    q.Exit to main menu
        
How can I help you?''')
        c=input("==>")
        if c=="q": break
        
        elif c=="1":
            print ("Where is the new school located?")
            location=input("==>")
            system.createSchool(location)
        
        elif c=="2":
            print ("What is the course name?")
            course_name=input("==>")
            print ("What is the price of this course?")
            price=input("==>")
            print ("How long will this course last in week?")
            period=input("==>")
            system.createCourse(course_name,price,period)
        
        elif c=="3":
            print ("Please enter the teacher's name")
            teacher_name=input("==>")
            print ("Please enter a passcode for authorization")
            passcode=input("==>").strip()
            school=util.chooseSchool()
            if school:
                system.createTeacher(teacher_name,passcode,school)
          
        elif c=="4":
            print ("Which school is the new section located in?")
            school=util.chooseSchool()
            if school:
                print ("What is the course of the new section?")
                course=util.chooseCourse()
                print ("Who is the teacher for the new section?")
                teacher=util.chooseTeacher(school)
                if course and teacher:
                    school.createSection(course,teacher)
                
while True:
    print('''----Welcome to the Class System----

    1.Student System
    2.Teacher System
    3.Admin System
    q.Exit Class System

How can I help you?''')

    c=input("==>")
    if c=="q":
        print("Exit successfully, thanks for using our system!")
        break
    elif c=="1":
        student_system()
    elif c=="2":
        teacher_system()
    elif c=="3":
        admin_system()
    else:
        print("Invalid Input. Please try again.")