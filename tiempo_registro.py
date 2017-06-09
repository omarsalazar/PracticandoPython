# coding=utf-8
from datetime import datetime
# Día, mes y año actuales.
ahora = datetime.now()
diahoy = int(ahora.day)
meshoy = int(ahora.month)
aniohoy = int(ahora.year)
fecha_registro = datetime(2016-10-19)# noqa
# Esto saca los días entre las fechas
diferencia = ahora - fecha_registro
print("Entre las dos fechas hay {} días.".format(diferencia.days))
