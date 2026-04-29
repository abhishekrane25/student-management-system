# Student Management System Python Project
# Technologies: Core Python, MySQL and PDBC

# Package Import 
import mysql.connector # MYSQL Connector for Database Connectivity

# Database Query Functions
# 
def fetch_last_student_roll_no():
    cursor.execute("SELECT student_roll_no FROM students ORDER BY student_roll_no DESC LIMIT 1" )
    student_roll_no = cursor.fetchone()[0]
    return student_roll_no 

#
def add_student_record(student_roll_no, student_name, student_address, student_grade):
    
    try:
        cursor.execute("INSERT INTO students (student_name, student_address, student_grade) VALUES(%s, %s, %s)", ( student_name, student_address, int(student_grade) ) )
        conn.commit()

    except Exception as e:
         print("Error Message:", e)
    
    finally: 
        print("Student roll no: ", student_roll_no +1, " record added.")
        


try: 
    # Database Connector 
    conn = mysql.connector.connect(
            host = "localhost",
            username = "root",
            password = "root",
            database = "student_management_system_database"
    )
    

    # Database Cursor
    cursor = conn.cursor()
    try:
                # Loop Till End Of Program
        while True:

        # Display Message
            print("Welcome to Student Management System")
            print("1. Add Student")
            print("2. View Student by Roll No.")
            print("3. View All Students")
            print("4. Update Student Information")
            print("5. Delete Student Record")

            choice = int(input("Please enter your choice: "))

        # Conditional Statement for different User Choices
            match choice:
                # `Add Student` Module
                case 1:
                        print("Add Student Record")                 
                        student_roll_no = fetch_last_student_roll_no()
                        print("Student roll no: ", student_roll_no + 1)
                        student_name = input("Enter name of the student (Firstname Lastname): ")
                        student_address = input("Enter residential address of student (Landmark, City Name):")
                        student_grade = int(input("Enter grade of Student (1-10):"))
                        add_student_record(student_roll_no, student_name, student_address, student_grade)
                        break
                
    except Exception as e:
         print(e)
    
    finally:
            print("\nSystem Closed.")


except Exception as e:
    print(e)

finally:
    print("\nConnection closed.")
    conn.close()


