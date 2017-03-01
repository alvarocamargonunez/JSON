#!/usr/bin/python
#-*- coding: utf-8 -*--
#5) Introduce un numero de puestos determinados y muestra los mercados con ese numero de puestos.
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import json
from pprint import pprint
fichero=open("/home/alvarocamargo/Descargas/segundo año/lenguaje de marcas/mercados.json","r")
lineas=json.load(fichero)
numero=int(raw_input("Introduce un numero de puestos determinado:"))
hay=False
for x in lineas:
	
	