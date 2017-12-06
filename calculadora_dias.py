# coding=utf-8
from datetime import datetime

global hoy
hoy = datetime.now()
diahoy = int(hoy.day)
meshoy = int(hoy.month)
aniohoy = int(hoy.year)

def caso1():
	dia = int(input("Ingresa el dia \n"))
	mes = int(input("Ingresa el mes \n"))
	anio = int(input("Ingresa el año \n"))
	fecha = datetime(anio, mes, dia)
	diferencia = hoy - fecha
	print("Entre {} y {} hay {} días.".format(hoy.days, fecha, diferencia.days))

print("Bienvenido al calculador de días y fechas\n¿Qué quieres hacer?\n")
eleccion = input("1- Saber cuantos días han pasado desde una fecha.\n2- Saber la cantidad de días entre dos fechas")#noqa

if eleccion == 1:
	caso1()