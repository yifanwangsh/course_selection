import School
import Admin_system

def chooseSchool():
    system=Admin_system.Admin_system
    school_info=system.listSchool()
    return _choose(school_info,"school")

def chooseCourse():
    system=Admin_system.Admin_system
    course_info=system.listCourse()
    return _choose(course_info,"course")

def chooseTeacher(school):
    if not isinstance(school,School.School):
        raise TypeError("Rejected")
    
    teacher_info=school.listTeacher()
    return _choose(teacher_info,"teacher")     

def _choose(dict,name):
    key_list=list(dict.keys())
    while True:
        print ("The following " + name + " is available:")
        for i in range(len(key_list)):
            print (str(i+1) + "." + key_list[i])
        print ("Please choose a " + name + ". Press q to quit")
        inp=input("==>")
        if inp=="q":return
        s=int(inp)-1
        if s in range(len(key_list)):
            return dict[key_list[s]]
        else:
            print ("Invalid choice")

def listKeys(key_list):
    for i in range(len(key_list)):
        print (str(i+1) + "." + key_list[i])
    print ("\n")