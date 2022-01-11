from tkinter import *
from tkinter import ttk
import sqlite3

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

label6 = Label(frame, text='   HH  :  MM',fg='grey')
label6.grid(row='4',column= '0',columnspan=2,sticky="W",pady=(20,0))

label6 = Label(frame, text=' HH  :  MM',fg='grey')
label6.grid(row='4',column= '1',columnspan=2,sticky="E",pady=(20,0))

label4 = Label(frame, text='Task description:')
label4.grid(row='5',column= '0',columnspan=4,sticky="W",pady=(40,0))

label5 = Label(frame, text='Software to use:')
label5.grid(row='7',column= '0',columnspan=4,sticky="W",pady=(20,0))


#------------- entrys -------------

task_name = Entry (frame,width=30)
task_name.grid(row='1',column= '0',columnspan=3)

entry1 = ttk.Spinbox(from_=1, to=24,state='readonly')
entry1.place(x=20, y=110, width=40)

entry2 = ttk.Spinbox(from_=0, to=59,state='readonly')
entry2.place(x=60, y=110, width=40)

entry3 = ttk.Spinbox(from_=1, to=24,state='readonly')
entry3.place(x=140, y=110, width=40)

entry4 = ttk.Spinbox(from_=0, to=59,state='readonly')
entry4.place(x=180, y=110, width=40)

entry5 = Text (frame,width=30,height=5,font=("Arial", "10"))
entry5.grid(row='6',column= '0',columnspan=4,ipady=50)

def getResults():

    # get a tuple with the entries
    e = task_name.get(),entry1.get(), entry2.get(), entry3.get(),entry4.get(), entry5.get("1.0",END)
    print(e)
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE tasks(
            name text,
            fromH integer,
            fromM integer,
            toH integer,
            toM integer,
            description text
    )""")
    conn.commit()
    conn.close()

    # check if any field is empty
    for i in e:
        if i == '':
            print('error!')
        print(i)



getbutton = Button(frame)
getbutton.configure(text='Ok',command=getResults)
getbutton.grid(row='10',column= '0',columnspan=3,pady=(20,0))

# infinite loop, interrupted by keyboard or mouse
mainloop()