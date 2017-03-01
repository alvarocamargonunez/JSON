#!/usr/bin/python
#-*- coding: utf-8 -*--
#4)Introduce una subcadena y si coincide con la pedania de los mercados muestre el nombre y la direccion.
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import json
from pprint import pprint


fichero=open("mercados.json","r")
datos=json.load(fichero)
empieza=raw_input("Introduce el comienzo del nombre de la pedanía que desea buscar:")

