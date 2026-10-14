import curses

def get_input(stdscr, y, x, prompt):
    stdscr.addstr(y, x, prompt)
    curses.echo()
    user_input = stdscr.getstr(y, x + len(prompt), 30).decode('utf-8')
    curses.noecho()
    return user_input