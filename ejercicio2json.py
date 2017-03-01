#!/usr/bin/python
#-*- coding: utf-8 -*--
#2)Programa que muestre el numero de mercados.
import json
with open("mercados.json","r") as fichero:
	doc=json.load(fichero)



cont=0
for r in doc:
	if r["tipo"]=="MERCADO SEMANAL" or r["tipo"]=="PLAZA DE ABASTOS":
	

