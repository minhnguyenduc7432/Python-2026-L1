import curses
import os
import zipfile
from domains.course import Course
from domains.student import Student
from input import get_input
from output import show_students

def load_data(students, courses):
    if not os.path.exists("students.dat"):
        return

    with zipfile.ZipFile("students.dat", "r") as zf:
        zf.extractall()

    if os.path.exists("courses.txt"):
        with open("courses.txt", "r") as f:
            for line in f:
                c_id, name, credits = line.strip().split(",")
                courses[c_id] = Course(c_id, name, int(credits))

    if os.path.exists("students.txt"):
        with open("students.txt", "r") as f:
            for line in f:
                s_id, name, dob = line.strip().split(",")
                students.append(Student(s_id, name, dob))

    if os.path.exists("marks.txt"):
        with open("marks.txt", "r") as f:
            for line in f:
                s_id, c_id, mark = line.strip().split(",")
                student = next((s for s in students if s.s_id == s_id), None)
                if student:
                    student.marks[c_id] = float(mark)

    if os.path.exists("courses.txt"): os.remove("courses.txt")
    if os.path.exists("students.txt"): os.remove("students.txt")
    if os.path.exists("marks.txt"): os.remove("marks.txt")

def save_and_compress_data(students, courses):
    with open("courses.txt", "w") as f:
        for c in courses.values():
            f.write(f"{c.c_id},{c.name},{c.credits}\n")
            
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s.s_id},{s.name},{s.dob}\n")
            
    with open("marks.txt", "w") as f:
        for s in students:
            for c_id, mark in s.marks.items():
                f.write(f"{s.s_id},{c_id},{mark}\n")

    with zipfile.ZipFile("students.dat", "w") as zf:
        zf.write("courses.txt")
        zf.write("students.txt")
        zf.write("marks.txt")
        
    if os.path.exists("courses.txt"): os.remove("courses.txt")
    if os.path.exists("students.txt"): os.remove("students.txt")
    if os.path.exists("marks.txt"): os.remove("marks.txt")

def main_app(stdscr):
    students = []
    courses = {}
    
    load_data(students, courses)

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "=== STUDENT MARK MANAGEMENT ===", curses.A_BOLD)
        stdscr.addstr(2, 0, "1. Add a Course")
        stdscr.addstr(3, 0, "2. Add a Student")
        stdscr.addstr(4, 0, "3. Input Marks for a Student")
        stdscr.addstr(5, 0, "4. Show Students (Sorted by GPA)")
        stdscr.addstr(6, 0, "5. Exit and Save Data")
        
        choice = get_input(stdscr, 8, 0, "Enter your choice (1-5): ")

        if choice == '1':
            stdscr.clear()
            c_id = get_input(stdscr, 0, 0, "Course ID: ")
            name = get_input(stdscr, 1, 0, "Course Name: ")
            credits_str = get_input(stdscr, 2, 0, "Credits: ")
            try:
                credits = int(credits_str)
                courses[c_id] = Course(c_id, name, credits)
                stdscr.addstr(4, 0, "Course added! Press any key...", curses.A_BOLD)
            except ValueError:
                stdscr.addstr(4, 0, "Invalid credits! Press any key...")
            stdscr.getch()

        elif choice == '2':
            stdscr.clear()
            s_id = get_input(stdscr, 0, 0, "Student ID: ")
            name = get_input(stdscr, 1, 0, "Student Name: ")
            dob = get_input(stdscr, 2, 0, "Date of Birth: ")
            students.append(Student(s_id, name, dob))
            stdscr.addstr(4, 0, "Student added! Press any key...", curses.A_BOLD)
            stdscr.getch()

        elif choice == '3':
            stdscr.clear()
            s_id = get_input(stdscr, 0, 0, "Enter Student ID: ")
            c_id = get_input(stdscr, 1, 0, "Enter Course ID: ")
            
            student = next((s for s in students if s.s_id == s_id), None)
            
            if student and c_id in courses:
                mark_str = get_input(stdscr, 2, 0, "Enter Mark: ")
                try:
                    mark = float(mark_str)
                    student.add_mark(c_id, mark)
                    stdscr.addstr(4, 0, "Mark added! Press any key...")
                except ValueError:
                    stdscr.addstr(4, 0, "Invalid mark! Press any key...")
            else:
                stdscr.addstr(4, 0, "Student or Course not found! Press any key...")
            stdscr.getch()

        elif choice == '4':
            show_students(stdscr, students, courses)

        elif choice == '5':
            save_and_compress_data(students, courses)
            break

if __name__ == "__main__":
    curses.wrapper(main_app)