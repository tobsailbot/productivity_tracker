# class Task():
#
#     def __init__(self):
#         self.name = None
#         self.time = None
#         self.info = None
#
#     def createTask(self):
#         print('ingrese nombre de la nueva task: ')
#         task_name = input()
#         self.name = task_name
#
#     def getInfo(self):
#         print('la nueva tarea es: ')
#         print(self.name)
#
#
# task = Task()
#
# task.createTask()
# task.getInfo()

# Imports tkinter and ttk module
from tkinter import *
from tkinter.ttk import *

# toplevel window
root = Tk()


# method to make widget invisible
# or remove from toplevel
def forget(widget):
    # This will remove the widget from toplevel
    # basically widget do not get deleted
    # it just becomes invisible and loses its position
    # and can be retrieve
    widget.forget()


# method to make widget visible
def retrieve(widget):
    widget.pack(fill=BOTH, expand=True)


# Button widgets
b1 = Button(root, text="Btn 1")
b1.pack(fill=BOTH, expand=True)

# See, in command forget() method is passed
b2 = Button(root, text="Btn 2", command=lambda: forget(b1))
b2.pack(fill=BOTH, expand=True)

# In command retrieve() method is passed
b3 = Button(root, text="Btn 3", command=lambda: retrieve(b1))
b3.pack(fill=BOTH, expand=True)

# infinite loop, interrupted by keyboard or mouse
mainloop()