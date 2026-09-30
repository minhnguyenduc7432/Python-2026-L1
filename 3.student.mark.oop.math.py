import math
import numpy as np
import curses

class Course:
    def __init__(self, c_id, name, credits):
        self.c_id = c_id
        self.name = name
        self.credits = credits

class Student:
    def __init__(self, s_id, name, dob):
        self.s_id = s_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0

    def add_mark(self, course_id, mark):
        self.marks[course_id] = math.floor(mark * 10) / 10.0

    def calculate_gpa(self, courses_dict):
        if not self.marks:
            self.gpa = 0.0
            return
        
        marks_arr = []
        credits_arr = []
        
        for c_id, mark in self.marks.items():
            if c_id in courses_dict:
                marks_arr.append(mark)
                credits_arr.append(courses_dict[c_id].credits)
                
        if marks_arr:
            np_marks = np.array(marks_arr)
            np_credits = np.array(credits_arr)
            self.gpa = np.average(np_marks, weights=np_credits)

def get_input(stdscr, y, x, prompt):
    stdscr.addstr(y, x, prompt)
    curses.echo()
    user_input = stdscr.getstr(y, x + len(prompt), 30).decode('utf-8')
    curses.noecho()
    return user_input

def main_app(stdscr):
    students = []
    courses = {}

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "=== STUDENT MARK MANAGEMENT ===", curses.A_BOLD)
        stdscr.addstr(2, 0, "1. Add a Course")
        stdscr.addstr(3, 0, "2. Add a Student")
        stdscr.addstr(4, 0, "3. Input Marks for a Student")
        stdscr.addstr(5, 0, "4. Show Students (Sorted by GPA)")
        stdscr.addstr(6, 0, "5. Exit")
        
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
                    stdscr.addstr(4, 0, f"Mark added: {student.marks[c_id]}! Press any key...")
                except ValueError:
                    stdscr.addstr(4, 0, "Invalid mark! Press any key...")
            else:
                stdscr.addstr(4, 0, "Student or Course not found! Press any key...")
            stdscr.getch()

        elif choice == '4':
            stdscr.clear()
            stdscr.addstr(0, 0, "=== STUDENT LIST (SORTED BY GPA) ===", curses.A_BOLD)
            
            for s in students:
                s.calculate_gpa(courses)
            students.sort(key=lambda x: x.gpa, reverse=True)

            row = 2
            stdscr.addstr(row, 0, f"{'ID':<10} | {'Name':<20} | {'GPA':<5}")
            row += 1
            stdscr.addstr(row, 0, "-"*40)
            row += 1
            
            for s in students:
                stdscr.addstr(row, 0, f"{s.s_id:<10} | {s.name:<20} | {s.gpa:.1f}")
                row += 1

            stdscr.addstr(row + 2, 0, "Press any key to return...")
            stdscr.getch()

        elif choice == '5':
            break

if __name__ == "__main__":
    curses.wrapper(main_app)