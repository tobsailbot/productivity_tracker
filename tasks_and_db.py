from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

window = Tk()

global data_base
data_base = None

class NewWindow(Toplevel):

    def __init__(self, window=None):
        super().__init__(master=window)
        self.grab_set()
        window.resizable(False, False)
        # window.geometry(f'{150}x{67}+{screen_x}+{0}')  # window size(x) and position (+)

        # frame widget
        self.frame = Frame(self)
        self.frame.pack(fill=BOTH, pady=10, padx=20)

        # --------- labels -----------
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

        # ------------- entrys -------------

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

                conn = sqlite3.connect('tasks.db')
                c = conn.cursor()
                # insert the values into the db table
                c.execute("INSERT INTO tasks VALUES (:name, :fromH, :fromM, :toH, :toM, :description)",
                              {
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
                self.newTaskSlot()





    def showResults(self):

            conn = sqlite3.connect('tasks.db')
            c = conn.cursor()

            c.execute("SELECT * FROM tasks")
            global data_base
            data_base = c.fetchall()[-1]

            conn.commit()
            conn.close()
            print(data_base)

    def newTaskSlot(self):

        # Task Frame
        window.task_frame = Frame(window, bg='grey',highlightbackground="black",highlightthickness=1)
        window.task_frame.pack(fill=BOTH, pady=(10,0), padx=20)

        # Task Name
        window.task_name = Label(window.task_frame, text=data_base[0])
        window.task_name.pack(side=LEFT)

        # Task Time
        window.task_time = Label(window.task_frame, text=f'{data_base[1]}:{data_base[2]} - {data_base[3]}:{data_base[4]}')
        window.task_time.pack(side=RIGHT)

        # Task description Frame
        window.task_desc_frame = Frame(window, bg='grey',highlightbackground="black",highlightthickness=1)
        window.task_desc_frame.pack(fill=BOTH, padx=20)

        # Define a function to show/hide widget
        def show_wg():
            window.task_desc.pack()
            window.show_desc.pack_forget()
            window.hide_desc.pack()

        def hide_wg():
            window.task_desc.pack_forget()
            window.show_desc.pack()
            window.hide_desc.pack_forget()

        # Task Description
        window.task_desc = Label(window.task_desc_frame, text=data_base[5])

        # Hide Description
        window.hide_desc = Button(window.task_desc_frame)
        window.hide_desc.configure(text='^',width=50,height=1, command= hide_wg)

        # Show Description
        window.show_desc = Button(window.task_desc_frame)
        window.show_desc.configure(text='v',width=50,height=1, command= show_wg)
        window.show_desc.pack(ipady=1)


window.title("Productivity Tracker")
window.geometry("400x800")

# def show_widget():
#    task_desc.pack()
# def hide_widget():
#    label.pack_forget()
#    b1.configure(text="Show", command=show_widget)

def createTaskWindow():
    NewWindow(window)

new_task = Button(window,text='New task')
new_task.configure(text='New task', command=createTaskWindow)
new_task.pack()

# NewWindow(window)

mainloop()