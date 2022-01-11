from tkinter import *
from tkinter import ttk

window = Tk()

# calculate the screen width based on the resolution
screen_width = window.winfo_screenwidth()
screen_x= int(screen_width/2)

window.resizable(False,False)
#window.geometry(f'{150}x{67}+{screen_x}+{0}')  # window size(x) and position (+)

# frame widget
frame = Frame(window)
frame.pack(fill=BOTH,pady=10,padx=20)

label1 = Label(frame, text='Task name:')
label1.grid(row='0',column= '0',columnspan=4,sticky="W",pady=(20,0))

label2 = Label(frame, text='From')
label2.grid(row='2',column= '0',columnspan=4,sticky="W",pady=(20,0))

label3 = Label(frame, text='To')
label3.grid(row='2',column= '2',columnspan=4,sticky="W",pady=(20,0))

label4 = Label(frame, text='Task description:')
label4.grid(row='4',column= '0',columnspan=4,sticky="W",pady=(20,0))

label5 = Label(frame, text='Software to use:')
label5.grid(row='6',column= '0',columnspan=4,sticky="W",pady=(20,0))

#------------- entrys -------------

task_name = Entry (frame,width=20)
task_name.grid(row='1',column= '0',columnspan=3)
task_name.insert(0, "This is the default text")

entry2 = ttk.Spinbox(from_=1, to=24,state='readonly')
entry2.place(x=105, y=30, width=70)
# entry2["values"] = ["01:00", "02:00", "C++", "Java"]

entry3 = ttk.Combobox(frame,width=4)
entry3.grid(row='3',column= '1')
entry3["values"] = ["Python", "C", "C++", "Java"]

entry3 = ttk.Combobox(frame,width=4)
entry3.grid(row='3',column= '2')
entry3["values"] = ["Python", "C", "C++", "Java"]

entry3 = ttk.Combobox(frame,width=4)
entry3.grid(row='3',column= '3')
entry3["values"] = ["Python", "C", "C++", "Java"]

entry4 = Text (frame,width=20,height=5,font=("Arial", "10"))
entry4.grid(row='5',column= '0',columnspan=4,ipady=50)

def getResults():
    e = task_name.get(), entry2.get(), entry3.get(), entry4.get("1.0",END),
    print(e)

getbutton = Button(frame)
getbutton.configure(text='Ok',command=getResults)
getbutton.grid(row='10',column= '0',columnspan=3,pady=(20,0))

# infinite loop, interrupted by keyboard or mouse
mainloop()