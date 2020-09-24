import time
import curses

def main(stdscr):
    curses.curs_set(0)
    stdscr.refresh()
    show_list(stdscr)

def show_list(stdscr):
    numbers = ['a', 'b', 'c']
    for i in range(len(numbers)):
        stdscr.addstr(i, 5, numbers[i-1]) 
        stdscr.refresh()
    time.sleep(5)

curses.wrapper(main)

