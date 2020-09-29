import time
import curses

def main(stdscr):
    curses.curs_set(0)
    stdscr.refresh()
    numbers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    # numbers = ['a', 'b', 'c'] 
    begin_x = 20; begin_y = 7
    height = 5; width = 40
    curwin = curses.newwin(height, width, begin_y, begin_x)
    curwin.box(0, 0)
    show_list(curwin, numbers, 0)
    scroll_list(curwin, numbers, 1)
    scroll_list(curwin, numbers, 2)

def show_list(curwin, entries, pos):
    for i in range(curwin.getmaxyx()[0] - 2):
        try: 
            curwin.addstr(i+1+pos, 5, entries[i]) 
        except:
            print('FAILED')
        curwin.refresh()
    time.sleep(2)

def scroll_list(curwin, entries, pos):
    curwin.clear()
    pos += 1
    show_list(curwin, entries, pos)

curses.wrapper(main)

