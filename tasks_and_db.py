from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime
import sqlite3

window = Tk()

global data_base
data_base = None

# ------------ New Task Top Level window -----------------

class NewTask(Toplevel):

    def __init__(self, window=None):
        super().__init__(master=window)
        # Creates an unique window instance
        self.grab_set()
        # Not resizable
        self.resizable(False, False)
        self.title("New Task")

        # frame widget
        self.frame = Frame(self)
        self.frame.pack(fill=BOTH, pady=10, padx=20)

        # -------------------- labels --------------------------

        self.label1 = Label(self.frame, text='Task name:')
        self.label1.grid(row='0', column='0', columnspan=4, sticky="W", pady=(20, 0))

        self.label2 = Label(self.frame, text='From')
        self.label2.grid(row='2', column='0', columnspan=4, sticky="W", pady=(20, 0))

        self.label3 = Label(self.frame, text='To')
        self.label3.grid(row='2', column='2', columnspan=4, sticky="W", pady=(20, 0))

        self.label6 = Label(self.frame, text='   HH  :  MM', fg='grey')
        self.label6.grid(row='4', column='0', columnspan=2, sticky="W", pady=(20, 0))

        self.label6 = Label(self.frame, text=' HH  :  MM', fg='grey')
        self.label6.grid(row='4', column='1', columnspan=2, sticky="E", pady=(20, 0))

        self.label4 = Label(self.frame, text='Task description:')
        self.label4.grid(row='5', column='0', columnspan=4, sticky="W", pady=(40, 0))

        self.label5 = Label(self.frame, text='Software to use:')
        self.label5.grid(row='7', column='0', columnspan=4, sticky="W", pady=(20, 0))

        # --------------------- entrys -------------------------

        self.name = Entry(self.frame, width=30)
        self.name.grid(row='1', column='0', columnspan=3)

        self.fromH = ttk.Spinbox(self.frame,from_=1, to=24)
        self.fromH.place(x=0, y=104, width=40)

        self.fromM = ttk.Spinbox(self.frame,from_=0, to=59)
        self.fromM.place(x=40, y=104, width=40)

        self.toH = ttk.Spinbox(self.frame,from_=1, to=24)
        self.toH.place(x=120, y=104, width=40)

        self.toM = ttk.Spinbox(self.frame,from_=0, to=59)
        self.toM.place(x=160, y=104, width=40)

        self.description = Text(self.frame, width=30, height=5, font=("Arial", "10"))
        self.description.grid(row='6', column='0', columnspan=4, ipady=50)

        self.getbutton = Button(self.frame)
        self.getbutton.configure(text='Ok', command=self.commitResults)
        self.getbutton.grid(row='10', column='0', columnspan=3, pady=(20, 0))

    def commitResults(self):

            # get a tuple with the entries
            e = self.name.get(), self.fromH.get(), self.fromM.get(), self.toH.get(), self.toM.get(), self.description.get("1.0", END)

            # if any field is empty...
            if all(e) == False:
                print('--- Empty field!')
                empty_field = messagebox.showinfo(message=f"Error empty field", title="Título")
            else:
                print('--- Commit to database')

                # Connect to the database.db file
                conn = sqlite3.connect('tasks.db')
                c = conn.cursor()
                # Insert the values into the db table
                c.execute("INSERT INTO tasks VALUES (:id, :name, :fromH, :fromM, :toH, :toM, :description)",
                              {
                                  'id': None,
                                  'name': self.name.get(),
                                  'fromH': self.fromH.get(),
                                  'fromM': self.fromM.get(),
                                  'toH': self.toH.get(),
                                  'toM': self.toM.get(),
                                  'description': self.description.get("1.0", END)
                              })
                conn.commit()
                conn.close()

                self.destroy()
                self.showResults()

        #------------- functions inside newTask window ----------------


    def showResults(self):

            conn = sqlite3.connect('tasks.db')
            c = conn.cursor()

            c.execute("SELECT * FROM tasks")
            new_task = c.fetchall()[-1]
            NewTaskFrame(new_task[0],new_task[1],new_task[2],new_task[3],new_task[4],new_task[5],new_task[6])
            global data_base
            data_base = c.fetchall()
            conn.commit()
            conn.close()



#-------------------------- New Task frame class -------------------------------

class NewTaskFrame(Frame):
    def __init__(self,id, name, fromH, fromM, toH, toM, desc, **kwargs):
        # pack into main_frame
        Frame.__init__(self,main_frame)

        # Task Frame
        self.configure(highlightbackground="grey",highlightthickness=1)
        self.pack(fill=BOTH, pady=(10,0), padx=20)

        # Task Name
        self.task_name = Label(self, text=name)
        self.task_name.grid(row=0,column=0,sticky='W',padx=(10,0))

        # Task Time
        self.task_time = Label(self, text=f'{fromH}:{fromM} - {toH}:{toM}')
        self.task_time.grid(row=0,column=0,sticky='E',padx=(0,10))

        # Get the row 'id' of the database
        self.id = id

        def deleteFrame():
            MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to delete this task?',icon='warning')
            if MsgBox == 'yes':
                self.pack_forget()
                conn = sqlite3.connect('tasks.db')
                c = conn.cursor()
                c.execute("DELETE FROM tasks where id=(?)", (self.id,))
                conn.commit()
                conn.close()
            else:
                return

        self.delete_btn = Button(self)
        self.delete_btn.configure(text='Delete Task',command=deleteFrame)
        self.delete_btn.grid(sticky='E')

        # Task description Frame
        self.task_desc_frame = Frame(self,highlightbackground="black",highlightthickness=0)
        self.task_desc_frame.grid()

        # Define a function to show/hide widget
        def show_wg():
            self.hide_desc.grid(row=1,column=0)
            self.task_desc.grid(row=2,column=0,pady=(10,0))
            self.show_desc.grid_remove()

        def hide_wg():
            self.task_desc.grid_remove()
            self.show_desc.grid(row=2,column=0)
            self.hide_desc.grid_remove()

        # Task Description Label
        self.task_desc = Label(self.task_desc_frame, text=desc)

        # Hide Description Button
        self.hide_desc = Button(self.task_desc_frame)
        self.hide_desc.configure(text='^',width=50,height=1,bd=0.5, command= hide_wg)

        # Show Description Button
        self.show_desc = Button(self.task_desc_frame)
        self.show_desc.configure(text='v',width=50,height=-10,bd=0.5, command= show_wg)
        self.show_desc.grid(row=1,column=0)



# ----------------------- Main Window ------------------------

# Main window properties
window.title("Productivity Tracker")
# window.geometry("400x400")
# Resize only vertical
window.resizable(False,True)
window.configure(bg='grey64')

# Creates the main Frame that contains all the Task frames
main_frame = Frame(window)
main_frame.configure(height=50,bg='grey64')
main_frame.pack(fill=BOTH)

# show saved tasks from the database into the main window
def fetchDataBase():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    global data_base
    data_base = c.fetchall()
    conn.commit()
    conn.close()
    # Check if there is no rows in the database at start
    if data_base == []:
        print('no tasks')
        window.geometry("400x150")

# Run the function
fetchDataBase()

# Create the newTaskwindow
def createTaskWindow():
    NewTask(window)



# Button to create New Task
new_task = Button(window)
new_task.configure(text='Add Task', command=createTaskWindow)
new_task.pack(pady=(5,10))

# Takes the global variable 'data_base', creates the NewFrameTask and pass the arguments
for i in data_base:
    btn1 = NewTaskFrame(i[0],i[1],i[2],i[3],i[4],i[5],i[6])



#-------------------- Date Time activate task -------------------------

global actual_time
actual_time = str(datetime.datetime.now())


def actualTime():
    global actual_time
    actual_time = str(datetime.datetime.now())
    # Extract the hours an minutes
    hour_now = int(actual_time[11:13])
    min_now = int(actual_time[14:16])
    sec_now = int(actual_time[17:19])
    print(f'horas: {hour_now}')
    print(f'minutes: {min_now}')
    # Fetch the database
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    data_base = c.fetchall()
    conn.commit()
    conn.close()
    # Check database times
    for i in data_base:
        print(i[2],i[3])
        if hour_now == i[2] and min_now == i[3]:
            print(True)
            print('Comenzar la taarea!')

# Calcular cuantas horas y minutos necesarios para realizar la tarea
def getTaskDuration():
    for i in data_base:
        hh = 0
        mm = 0

        # print(i[2], ':',i[3], '-',i[4], ':',i[5])

        # If the start minutes are greater than the end minutes…
        if i[3] > i[5]:
            hh = (i[4]) - 1
            mm = (i[5]) + 60
            mm = mm - (i[3])
            hh = hh - (i[2])
        # f sar minutes are lower than end minutes
        if i[3] <= i[5]:
            hh = i[4] - i[2]
            mm = i[5] - i[3]

        print(hh,':',mm)


def updateWindow():
    window.after(60000,actualTime)
    window.after(60000,updateWindow)

updateWindow()

mainloop()

