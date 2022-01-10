from tkinter import *

window = Tk()

# calculate the screen width based on the resolution
screen_width = window.winfo_screenwidth()
screen_x= int(screen_width/2)

window.resizable(False,False)
#window.geometry(f'{150}x{67}+{screen_x}+{0}')  # window size(x) and position (+)

# frame widget
frame = Frame(window,bg='light goldenrod')
frame.pack(fill=BOTH)

task_name = Label(frame, text='Time remaining...',font=('Arial', 14))
task_name.grid(row='0',column= '0',columnspan='2')

entry1 = Entry (frame)
entry1.grid(row='2',column= '0',columnspan='2')

entry2 = Entry (frame)
entry2.grid(row='3',column= '0',columnspan='2')

def getResults():
    e = entry1.get(), entry2.get()

    print(e)

getbutton = Button(frame)
getbutton.configure(command=getResults)
getbutton.grid(row='4',column= '0',columnspan='2')

# infinite loop, interrupted by keyboard or mouse
mainloop()