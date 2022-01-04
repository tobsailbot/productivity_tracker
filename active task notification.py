
from tkinter import *



#----------------------------------------------------------------------------------------

timer_enable = True

# ***** VARIABLES *****
# use a boolean variable to help control state of time (running or not running)
running = False
# time variables initially set to 0
hours, minutes, seconds = 2, 45, 0

# ***** FUNCTIONS *****
# start, pause, and reset functions will be called when the buttons are clicked
# start function
def start():
    global running
    if not running:
        update()
        running = True

# pause function
def pause():
    global running
    if running:
        # cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False

# reset function
def reset():
    global running
    if running:
        # cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False
    # set variables back to zero
    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0
    # set label back to zero
    stopwatch_label.config(text='00:00:00')


# update stopwatch function
def update():

    # update seconds with (addition) compound assignment operator
    global hours, minutes, seconds
    if seconds == 0:
        minutes -= 1
        seconds = 60
    if minutes == 0:
        hours -= 1
        minutes = 59
    if hours <0:
        hours=0
        seconds=0
        minutes=0
    seconds -= 1

    # format time to include leading zeros
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'

    # update timer label after 1000 ms (1 second)
    stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    # after each second (1000 milliseconds), call update function
    # use update_time variable to cancel or pause the time using after_cancel
    global update_time
    update_time = stopwatch_label.after(10, update)

    # make a break window when 1500 seconds have passed / 25 minutes
    update_break = int(update_time[6:])
    if update_break != 0:
        if update_break%200 == 0:
            print(update_break)
            print('hora del break')
            NewWindow(window)

    # stop if time = 0:0:0
    if hours==0 and minutes==0 and seconds == 0:
        print('time ends')
        stopwatch_label.after_cancel(update_time)

#----------------------------------------------------------------------------------------

# creates the Break notification window

class NewWindow(Toplevel):

    def __init__(self, window=None):
        super().__init__(master=window)

        self.title("New Window")
        self.geometry("200x200")

        label = Label(self, text="Break Time...")
        label.pack()

        # destroy window after 5 minutes / 300000 segundos
        break_time = self.after(300, lambda: self.destroy())
        print(break_time)



#----------------------------------------------------------------------------------------


# toplevel window
window = Tk()

window.geometry('200x400')

# frame widget
frame = Frame(window,bg='yellow')
frame.pack(fill=BOTH)


global stopwatch_label # modify the stopwatch from gloabal
stopwatch_label = Label(frame, text='00:10:30', font=('Arial', 20),bg="grey",fg="white" )  # show the clock an pack it
stopwatch_label.grid(row='1',column= '0',columnspan='2')


start()  #start the timer function



# infinite loop, interrupted by keyboard or mouse
mainloop()