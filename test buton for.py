# objetivo: crear un frame mediante una clase, y dentro del frame un boton, y un label, el boton debera poder cambiar el color del label del frame propio

from tkinter import *
from tkinter import ttk
window = Tk()

window.title("Productivity Tracker")
# window.geometry("400x500")

fetch_all = [('ESTO ES UN TEST', '', 2, 1, '', '\n'),
             ('3434', 3, 4, 4, '', '434\n'),
             ('hola gato xd', 2, 33, 2, 3, '\n'),
             ('Como hacer videos', 14, 30, 15, 0, 'hola gastoo\n'),
             ('Test 3', 15, 30, 12, 55, 'esto es un testeooooo\nasdasdasdajajajaja\n\n'), ('asdasdasd', 24, 4, 4, 24, 'asdasd\n'),
             ('34', 34, 4, 34, 34, '3434\n'), ('asdasd', 5, 5, 5, 23, '\n'),
             ('232323', 2, 2, 2, 4, '\n'), ('testeoo', 15, 30, 16, 55, 'esto es una descpcion de prueba xd\n'),
             ('probando la porongola xd', 15, 45, 16, 80, 'ghoalaohohohohlalal\n')]


class NewTaskFrame(Frame):
    def __init__(self, name, fromH, fromM, toH, toM, desc, **kwargs):
        super(NewTaskFrame, self).__init__()

        # Task Frame
        self.configure(highlightbackground="black",highlightthickness=1)
        self.pack(fill=BOTH, pady=(10,0), padx=20)

        # Task Name
        self.task_name = Label(self, text=name)
        self.task_name.grid(row=0,column=0,sticky='W',padx=(10,0))

        # Task Time
        self.task_time = Label(self, text=f'{fromH}:{fromM} - {toH}:{toM}')
        self.task_time.grid(row=0,column=0,sticky='E',padx=(0,10))

        # Task description Frame
        self.task_desc_frame = Frame(self,highlightbackground="black",highlightthickness=1)
        self.task_desc_frame.grid()

        # Define a function to show/hide widget
        def show_wg():
            self.hide_desc.grid(row=1,column=0)
            self.task_desc.grid(row=2,column=0)
            self.show_desc.grid_remove()

        def hide_wg():
            self.task_desc.grid_remove()
            self.show_desc.grid(row=2,column=0)
            self.hide_desc.grid_remove()

        # Task Description
        self.task_desc = Label(self.task_desc_frame, text=desc)

        # Hide Description
        self.hide_desc = Button(self.task_desc_frame)
        self.hide_desc.configure(text='^',width=50,height=1,bd=0, command= hide_wg)

        # Show Description
        self.show_desc = Button(self.task_desc_frame)
        self.show_desc.configure(text='v',width=50,height=-10,bd=0, command= show_wg)
        self.show_desc.grid(row=1,column=0)


def dothings():
    print('Button class worked')
    btn1.configure(bg='red')

for i in fetch_all:
    btn1 = NewTaskFrame(i[0],i[1],i[2],i[3],i[4],i[5])


mainloop()

