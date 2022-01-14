from tkinter import *

window = Tk()
scrollbar = Scrollbar(window)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(window, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

mainloop()