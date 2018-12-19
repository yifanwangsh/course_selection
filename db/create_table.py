import psycopg2

conn=psycopg2.connect(host="localhost",dbname="python",user="postgres",password="admin")
cursor=conn.cursor()

create_section_info_sql="CREATE TABLE section_info (id varchar NOT NULL PRIMARY KEY, course_name varchar NOT NULL, school_id varchar NOT NULL, teacher_id varchar NOT NULL, section_id integer NOT NULL)"
create_course_info_sql="CREATE TABLE course_info (id varchar NOT NULL PRIMARY KEY, name varchar NOT NULL, price integer NOT NULL, period integer NOT NULL)"
create_school_info_sql="CREATE TABLE school_info (id varchar NOT NULL PRIMARY KEY, location varchar NOT NULL)"
create_student_info_sql="CREATE TABLE student_info (id varchar NOT NULL PRIMARY KEY, name varchar NOT NULL, school_id varchar NOT NULL)"
create_student_auth_info_sql="CREATE TABLE student_auth_info (name varchar NOT NULL PRIMARY KEY, passcode varchar NOT NULL)"
create_teacher_info_sql="CREATE TABLE teacher_info (id varchar NOT NULL PRIMARY KEY, name varchar NOT NULL, school_id varchar NOT NULL)"
create_teacher_auth_info_sql="CREATE TABLE teacher_auth_info (name varchar NOT NULL PRIMARY KEY, passcode varchar NOT NULL)"

cursor.execute(create_section_info_sql)
cursor.execute(create_course_info_sql)
cursor.execute(create_school_info_sql)
cursor.execute(create_student_auth_info_sql)
cursor.execute(create_student_info_sql)
cursor.execute(create_teacher_auth_info_sql)
cursor.execute(create_teacher_info_sql)

conn.commit()
cursor.close()
conn.close()