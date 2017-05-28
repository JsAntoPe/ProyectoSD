import funcdropbox
import json
import os

with open('resultado.txt', 'r') as datos:
	with open('r_procesado.txt', 'w+') as procesado:
		for line in datos:
			if line != '][\n' and line != "{\"tags\": []}\n" and line != "{\"tags\": []},\n":

				procesado.write(line)

with open('r_procesado.txt', 'rb') as procesado:
	string = procesado.read()
	funcdropbox.subida(string)
os.remove('resultado.txt')
