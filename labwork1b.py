def input_number_of_students():
    n = int(input("Enter number of students: "))
    return n
def input_student_info():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter Date of Birth: ")
    return {"id": student_id, "name": student_name, "dob": student_dob}