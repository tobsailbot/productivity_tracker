
# objetivo: crear un frame mediante una clase, y dentro del frame un boton, y un label, el boton debera poder cambiar el color del label del frame propio

from tkinter import *
window = Tk()

window.title("Productivity Tracker")
window.geometry("400x500")

list = [0,1,2,3,4]

botones = {}

# por cada elemento en la lista, crear un elemento en el diccionario con el nombre del elemento de la lista

# def changeColor(btn_name):
#     btn_name.configure(bg='green')
#
# for i in list:
#     botones[i] = f'btn_{i}'
#     btn_name = botones[i]
#     botones[i] = Button(window)
#     botones[i].configure(text=btn_name, command=botones[i].configure(bg='green'))
#     botones[i].pack()
#
#
# print(botones)

lista = ['Task name','Time duration','description asdasdasd']


class FrameTask(Frame):
    def __init__(self,color **kwargs):

        super().__init__()
        self.pack(fill=BOTH,pady=20)
        self.configure(bg='grey',highlightbackground="black",highlightthickness=1)

        self.name = Label(self,text='holasdasd',bg='green')
        self.name.pack()

        self.button = Button(self)
        self.button.configure(text='rojo',command=lambda: self.changeColor(color) )
        self.button.pack()

        self.button2 = Button(self)
        self.button2.configure(text='verde', command=lambda: self.changeColor('green'))
        self.button2.pack()

    def changeColor(self,color):
        self.configure(bg=color)



def dothings():
    print('Button class worked')
    btn1.configure(bg='red')


btn1 = FrameTask()

btn2= FrameTask()


# class btn():
#     def __init__(self):
#         print(list)
#
#     def changeColor(self):
#
#     def makeBtn(self):
#         for i in list:
#             task = f'Task{i}'
#             boton = Button(window)
#             boton.pack()
#             boton.configure(text=task)
#
#
#
#
#
#
# botones = btn()
#
# botones.makeBtn()


mainloop()

