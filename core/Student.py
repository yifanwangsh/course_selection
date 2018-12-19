import Person
import Section

class Student(Person.Person):
    def __init__ (self, name, id):
        super().__init__(name, id)
    
    def enroll(self,section):
        if not isinstance(section,Section.Section):
            raise TypeError("Rejected")

        query_section_info_sql='''SELECT sec.course_name,sch.location,sec.section_id FROM section_info AS sec LEFT JOIN school_info AS sch ON sec.school_id=sch.id
                                    WHERE sec.id=\'''' + section.getId() + "\'"
        raw=super().readFromDB(query_section_info_sql)[0]
        table_name=raw[0]+"_in_"+raw[1]+"_"+str(raw[2])
        
        update_section_table_sql="INSERT INTO " + table_name + "(student_id) VALUES (\'" + self.getId() + "\')"
        super().writeToDB(update_section_table_sql)

    def paytuition(self,section):
        if not isinstance(section, Section.Section):
            raise TypeError("Rejected")
        
        query_section_info_sql='''SELECT sec.course_name,sch.location,sec.section_id FROM section_info AS sec LEFT JOIN school_info AS sch ON sec.school_id=sch.id
                                    WHERE sec.id=\'''' + section.getId() + "\'"
        raw=super().readFromDB(query_section_info_sql)[0]
        table_name=raw[0]+"_in_"+raw[1]+"_"+str(raw[2])

        update_tuition_pay_sql="UPDATE " + table_name + " SET tuition_paid = TRUE WHERE student_id=\'" +  self.getId() + "\'"
        super().writeToDB(update_tuition_pay_sql)
        print ("Tuition paid")