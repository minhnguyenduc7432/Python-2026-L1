import curses

def show_students(stdscr, students, courses):
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