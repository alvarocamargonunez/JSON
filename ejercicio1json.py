#!/usr/bin/python
#-*- coding: utf-8 -*--
#1) Programa que liste todas las pedanías de los mercados.
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import json
from pprint import pprint

fichero=open("mercados.json","r")
lineas=json.load(fichero)

for x in lineas:
	
	
	print "\n"
	print x["pedania"]
