from tkinter import *

timer_enable = False

class Task():

    def createTask(self):

        def taskName():

        def taskTime():

        def taskInfo():

    def taskStart(self):

    def taskTimeRemaining(self):

    def openSoftware(self):

    def taskFinish(self):






def StartWindow():
    global window
    window = Tk(className='Python Examples - Window Color')  # window title

    # changes the window default opacity 0 to 1
    win_opacity = 1

    # calculate the screen width based on the resolution
    screen_width = window.winfo_screenwidth()
    # screen_x = int(screen_width / 2) # take the screen width

    window.title('Productivity Tracker')
    window.attributes('-alpha', win_opacity)  # window opacity
    window.configure(bg='grey')  # window color
    # window.overrideredirect(1)  # borderless window
    window.attributes('-topmost', True)  # keep always on top
    window.geometry(f'{300}x{600}+{800}+{0}')  # window size(x) and position (+)

    main_frame = Frame(window,bg="blue",pady=10)
    main_frame.pack(fill='both', expand=1,side= 'left')  # frame packing
    # main_frame.config(bg="blue",pady=30)

    # canvas = Canvas(frame, height='25', width='25', bg='grey', highlightthickness=0)  # canvas for REC button
    # canvas.create_oval(20, 20, 3, 3, fill='red')
    # canvas.grid(row=0, column=0)

    task = Frame(main_frame, bg='red')
    task.pack(fill='y', side= 'left')

    task_1 = Label(task, text="Task 1",bg="green", fg="white")
    task_1.grid(row=0, column=0)
    #
    # task2 = Label(frame, text="Task 2",bg="green", fg="white")
    # task2.grid(row=1, column=0,pady=30, padx=100)
    #
    # time_interval = Label(frame, text="15:30 - 17:30",bg="green", fg="white")
    # time_interval.grid(row=0, column=1)

    if timer_enable == True:
        global stopwatch_label  # modify the stopwatch from gloabal
        stopwatch_label = Label(frame, text='00:00:00', font=('Arial', 20), bg="grey",fg="white")  # show the clock an pack it
        stopwatch_label.grid(row='1', column='0', columnspan='2')
        window.geometry(f'{140}x{60}+{screen_x}+{0}')
        start()  # start the timer function

    window.attributes('-alpha', win_opacity)
    window.attributes('-topmost', True)

    # window.bind('<ButtonRelease-1>', ClickRelease)
    # window.bind('<Button-1>', SaveLastClickPos)  # click to drag and drop window
    # window.bind('<B1-Motion>', Dragging)

    window.mainloop()


StartWindow()