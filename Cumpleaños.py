# coding=utf-8
from datetime import datetime, date, time, timedelta

ahora = datetime.now()

dia = int(input("Ingresa tu dia de nacimiento \n"))
mes = int(input("Ingresa tu mes de nacimiento \n"))
anio = int(input("Ingresa tu año de nacimiento \n"))

diahoy = int(ahora.day)
meshoy = int(ahora.month)
aniohoy = int(ahora.year)
edad = aniohoy - anio
fecha1 = ahora
fecha2 = datetime(aniohoy, mes, dia, 0, 0, 0)
fecha3 = datetime(aniohoy + 1, mes, dia, 0, 0, 0)
diferencia = fecha2 - fecha1
diferencia2 = fecha3 - fecha1


if( fecha2 > fecha1):
    print("¡Aún no es tu cumpleaños!")
    print("¡Faltan {} días para que cumplas años!".format(diferencia))

else:
    print("Tu cumpleaños ya fue, ahora tienes {} años uwu y faltan {} para tu cumpleaños".format(edad, diferencia2))
