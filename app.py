# Student Management System Python Project
# Technologies: Core Python, MySQL and PDBC

# Package Import 
import mysql.connector # MYSQL Connector for Database Connectivity

# Database Query Functions
def fetch_last_student_roll_no():
    student_roll_no = cursor.execute("SELECT student_roll_no FROM students" )
    return student_roll_no

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
                        print("Student roll no: ", student_roll_no+1)
                        student_name = input("Enter name of the student (Firstname Lastname): ")
                        student_address = input("Enter residential address of student (Landmark, City Name):")
                        student_grade = int(input("Enter grade of Student (1-10):"))


    except Exception as e:
         print(e)
    
    finally:
            print("\nSystem Closed.")


except Exception as e:
    print(e)

finally:
    print("\nConnection closed.")
    conn.close()


