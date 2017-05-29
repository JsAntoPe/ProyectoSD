from dropboxSubidaParaProcesar import dropbox_subida_parap
import celery
import pandas
import numpy
import os

with open('resultado.txt', 'r') as datos:
	with open('r_procesado.txt', 'w+') as procesado:
		for line in datos:
			if line != '][\n' and line != "{\"tags\": []}\n" and line != "{\"tags\": []},\n":

				procesado.write(line)

with open('r_procesado.txt', 'r') as procesado:
	"""array = pandas.DataFrame(data=numpy.array([0, 0, 0, 0, 0, 0]), 
			index=['Row1'],
			columns=['java', 'C#', 'javascript', 'python', 'html', 'php'],
			)"""
	array = pandas.DataFrame({
			'java' : 0,
 			'c#' : 0,
			'javascript' : 0,
			'python' : 0,
			'html' : 0,
			'php' : 0
	}, index=['Row1'])
	for line in procesado:
		if '\"java\"' in line: 
			array.set_value('Row1', 'java', array.loc['Row1', 'java']+1)
		if 'c#' in line: 
			array.set_value('Row1', 'c#', array.loc['Row1', 'c#']+1)
		if 'javascript' in line: 
			array.set_value('Row1', 'javascript', array.loc['Row1', 'javascript']+1)
		if 'python' in line: 
			array.set_value('Row1', 'python', array.loc['Row1', 'python']+1)
		if 'html' in line: 
			array.set_value('Row1', 'html', array.loc['Row1', 'html']+1)
		if 'php' in line: 
			array.set_value('Row1', 'php', array.loc['Row1', 'php']+1)
	
	dropbox_subida_parap.delay(array.to_json())

os.remove('resultado.txt')

	
