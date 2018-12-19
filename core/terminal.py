import Student
import Student_system
import Teacher_system
import Admin_system

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
            school=chooseSchool()
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
            while True:
                print ("The following sections are available:")
                listOptions(available_section_info)
                print ("Please choose which section you want to enroll in. Press q to quit")
                inp=input("==>")
                if inp=="q":return
                s=int(inp)-1
                if s in range(len(available_section_info)):
                    return school_info[location_list[s]]
        else:
            print ("Invalid choice. Rejected")



def teacher_system():
    pass

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
            school=chooseSchool()
            if school:
                system.createTeacher(teacher_name,passcode,school)
            
            

def chooseSchool():
    system=Admin_system.Admin_system
    school_info=system.listSchool()

    while True:
        print ("We have school in:")
        listOptions(school_info)
        print ("Please choose a school. Press q to quit")
        inp=input("==>")
        if inp=="q":return
        s=int(inp)-1
        if s in range(len(location_list)):
            return school_info[location_list[s]]
        else:
            print ("Invalid choice. Rejected")    

def listOptions(dict):
    key_list=list(dict.keys())
    for i in range(len(key_list)):
        print (str(i+1) + "." + key_list[i])

while True:
    print('''----Welcome to the Class System----

    1.Student System
    2.Teacher System
    3.Admin System
    q.Exit Class System

Please input your choice''')

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