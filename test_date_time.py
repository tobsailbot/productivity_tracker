# import datetime
# import sqlite3
#
# datetime = str(datetime.datetime.now())
# # Extract the hours an minutes
# hour_now = datetime[11:13]
# min_now = datetime[14:16]
#
# print(f'horas: {hour_now}')
# print(f'minutes: {min_now}')
#
#
#
# conn = sqlite3.connect('tasks.db')
# c = conn.cursor()
# c.execute("SELECT * FROM tasks")
# data_base = c.fetchall()
# conn.commit()
# conn.close()
#
#
# # Obtener las horas y minutos de la base de datos y comparar con el la hora actual
# def actualTime():
#     for i in data_base:
#         if hour_now == i[2] and min_now == i[3]:
#             print(True)
#         else:
#             print(False)
#
# # Calcular cuantas horas y minutos necesarios para realizar la tarea
# def TaskDuration():
#     for i in data_base:
#         hh = 0
#         mm = 0
#         print(i[2], ':',
#               i[3], '-',
#               i[4], ':',
#               i[5])
#         # If the start minutes are greater than the end minutes…
#         if i[3] > i[5]:
#             hh = (i[4]) - 1
#             mm = (i[5]) + 60
#             mm = mm - (i[3])
#             hh = hh - (i[2])
#         # f sar minutes are lower than end minutes
#         if i[3] <= i[5]:
#             hh = i[4] - i[2]
#             mm = i[5] - i[3]
#         print(hh,':',mm)



import os

os.system("python task_notification.py 2 32")





