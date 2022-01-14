
from tkinter import *
from tkinter import messagebox

#----------------------------------------------------------------------------------------

lastClickX = 0
lastClickY = 0

clickReleaseX = 0
clickReleaseY = 0

x = 0
y = 0

timer_enable = True

five_min = None

# ***** VARIABLES *****
# use a boolean variable to help control state of time (running or not running)
running = False
# time variables initially set to 0
hours, minutes, seconds = 0, 10, 5

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
        seconds = 59
    if minutes <= 0:
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
    update_time = stopwatch_label.after(1000, update)


    update_break = int(update_time[6:])
    if hours>0 or minutes>0 or seconds>0:
        if update_break != 0:
            # make a break window when 1500 seconds have passed / 25 minutes
            if update_break%500 == 0:
                print(update_break)
                print('hora del break')
                # set the five min break text label in seconds
                global five_min
                five_min= 300
                # creates the new window break
                BreakNotif(window)

    else:
        # when time stops
        print('time ends')
        stopwatch_label.config(text='00:00:00')
        stopwatch_label.after_cancel(update_time)
        FinishTaskNotif(window)
        window.destroy()

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

# creates the Break notification window for 5 minutes

class BreakNotif(Toplevel):

    def __init__(self, window=None):
        super().__init__(master=window)

        self.title("New Window")
        self.geometry("200x200")
        self.attributes('-topmost', True)
        self.attributes('-fullscreen',True)

        self.frame1 = Frame(self,bg='SteelBlue3')
        self.frame1.pack(fill=BOTH,expand=True)

        self.notification = Label(self.frame1,text='Break Time:...',font=('Digital-7', 40))
        self.notification.pack(expand=True)

        self.label1 = Label(
            self.frame1,
            text=self.time_string(),
            font=('Digital-7', 48))

        self.label1.pack(expand=True)

        # destroy the new window after xxx miliseconds / 300000
        self.after(3000, lambda: self.destroy())
        # run the function after xxx miliseconds
        self.label1.after(1000, self.update)
        

    def time_string(self):
        global five_min
        five_min -= 1
        five_min_float = float(five_min/60)
        return f'{five_min_float:.2f}'

    def update(self):
        """ update the label every 1 second """ # iterative function
        self.label1.configure(text=self.time_string())
        self.label1.after(1000, self.update)

#----------------------------------------------------------------------------------------

class FinishTaskNotif(Toplevel):

    def __init__(self, window=None):
        super().__init__(master=window)

        self.title("New Window")
        self.geometry("20x20")
        self.wm_state('iconic')
        if messagebox.askyesno(message="Did you finish the Task?", title="Time ends") == True:
            messagebox.showinfo(message="Congratulations!!!", title="Well Done!")

        #----------------------------------------------------------------------------------------

# snap window to borders function
def ClickRelease(event):
    resolutionX = window.winfo_screenwidth() # gets the actual screen resolution
    resolutionY = window.winfo_screenheight()
    global x, y
    if window.winfo_y() < 0:  # if the current window position is below 0 , then move the window
        window.geometry("+%s+%s" % (x, 0))
    if window.winfo_y() > (resolutionY-35):
        window.geometry("+%s+%s" % (x,(resolutionY-35)))
    if window.winfo_x() < 0:
        window.geometry("+%s+%s" % (0, y))
    if window.winfo_x() > (resolutionX-140):
        window.geometry("+%s+%s" % ((resolutionX-140), y))

# left click window dragging function
def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def Dragging(event):
    global x, y
    x, y = event.x - lastClickX + window.winfo_x(), event.y - lastClickY + window.winfo_y()
    window.geometry("+%s+%s" % (x , y))

#------------------------------------------------------------------------------------
# main window
window = Tk()

# calculate the screen width based on the resolution
screen_width = window.winfo_screenwidth()
screen_x= int(screen_width/2)

window.attributes('-topmost', True)
window.resizable(False,False)
window.overrideredirect(1) # borderless window
window.attributes('-alpha', 0.8)
window.geometry(f'{150}x{67}+{screen_x}+{0}')  # window size(x) and position (+)

# frame widget
frame = Frame(window,bg='light goldenrod')
frame.pack(fill=BOTH)

task_name = Label(frame, text='Time remaining...',font=('Arial', 14))
task_name.grid(row='0',column= '0',columnspan='2')

global stopwatch_label # modify the stopwatch from gloabal
stopwatch_label = Label(frame, text='00:10:30', font=('Arial', 20),bg="light goldenrod",fg="black" )  # show the clock an pack it
stopwatch_label.grid(row='1',column= '0',columnspan='2')


start()  #start the timer function

window.bind('<ButtonRelease-1>', ClickRelease)

window.bind('<Button-1>', SaveLastClickPos)  # click to drag and drop window
window.bind('<B1-Motion>', Dragging)


# infinite loop, interrupted by keyboard or mouse
mainloop()