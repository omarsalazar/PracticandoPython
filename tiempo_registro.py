# coding=utf-8
from datetime import datetime, date, time, timedelta

#Día, mes y año actuales.
diahoy = int(ahora.day)
meshoy = int(ahora.month)
aniohoy = int(ahora.year)

ahora = datetime.now()
fecha_registro = datetime(2016-10-19)
#Esto saca los días entre las fechas
diferencia = ahora - fecha_registro
print("Entre las dos fechas hay {} días.".format(diferencia.days))
