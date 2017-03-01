#!/usr/bin/python
#-*- coding: utf-8 -*--
#3)Introduce un identificador(DIA DE LA SEMANA) y muestra los mercados que montan los puestos ese día.
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import json
from pprint import pprint


fichero=open("/home/alvarocamargo/Descargas/segundo año/lenguaje de marcas/mercados.json","r")
