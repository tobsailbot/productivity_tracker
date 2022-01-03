class Task():

    def __init__(self):
        self.name = None
        self.time = None
        self.info = None

    def createTask(self):
        print('ingrese nombre de la nueva task: ')
        task_name = input()
        self.name = task_name

    def getInfo(self):
        print('la nueva tarea es: ')
        print(self.name)


task = Task()

task.createTask()
task.getInfo()

