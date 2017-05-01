#!/usr/bin/env python
# -*- coding: utf-8 -*-
from read_csv import read_csv
from draw_page import draw_page
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from config import cfg
from pandas import read_excel, Series
from numpy.random import seed, randint
import datetime
import locale
import sys
import os
import platform

reload(sys)
sys.setdefaultencoding('utf8')

if platform.system().lower() == 'windows':
	locale.setlocale(locale.LC_TIME, 'portuguese_brazil') # Windows
else:
	locale.setlocale(locale.LC_TIME, 'pt_BR.utf8') # Linux

	
def get_filename(filewithext):
	return os.path.splitext(filewithext)[0]	

anualistas = False

n_args = len(sys.argv)

# Se o mês for dado como argumento (numérico: 1..12), usa-o;
# se não, usa o mês seguinte ao atual.
if n_args >= 2:
    month = int(sys.argv[1])
    anualistas = month == 0
else:
    month = datetime.date.today().month + 1

# Se o ano for dado como argumento (numérico), usa-o;
# se não, usa o ano atual.
if n_args >= 3:
    year = int(sys.argv[2])
else:
    year = datetime.date.today().year



input_files = filter(lambda f: '.xlsx' in f, os.listdir(cfg['DEFAULT_INPUT_PATH']))

if len(input_files) == 0:
	print('Não há arquivos de entrada na pasta {}'.format(cfg['DEFAULT_INPUT_PATH']))
	
else:

	for input_filename in input_files:
	
		print('Gerando crachás do arquivo {}...'.format(input_filename))
		
		input_file = '{}/{}'.format(cfg['DEFAULT_INPUT_PATH'], input_filename)
		
		# Define os nomes dos dois arquivos de saída: um contendo os crachás (PDF)
		# e o outro, os segredos (XLSX).
		if anualistas:
			badges_filename = "{}/{}_{}.pdf".format(cfg['DEFAULT_OUTPUT_PATH'], get_filename(input_filename), year)
			secrets_filename = "{}/{}_{}_secrets.xlsx".format(cfg['DEFAULT_OUTPUT_PATH'], get_filename(input_filename), year)
		else:
			badges_filename = "{}/{}_{}-{}.pdf".format(cfg['DEFAULT_OUTPUT_PATH'], get_filename(input_filename), year, month)
			secrets_filename = "{}/{}_{}-{}_secrets.xlsx".format(cfg['DEFAULT_OUTPUT_PATH'], get_filename(input_filename), year, month)
	
		pdf = canvas.Canvas(badges_filename)
		pdf.setFillColor(cfg['COLOR'])
		pdf.setFont(cfg['FONT_FAMILY'], cfg['FONT_SIZE'])

		SECRET_COL_NAME = 'Segredo'

		# Cria um DataFrame com os números de matrícula e nomes dados
		# e escolhe aleatoriamente os segredos.
		people = read_excel(input_file, sheetname=0)
		seed(int(year + month))
		people[SECRET_COL_NAME] = Series(randint(0,100000,size=len(people)))
		people.to_excel(secrets_filename, index=False)

		# Gera cada uma das imagens, de 4 em 4 associados
		associates = []
		count = 1

		if anualistas:
			month_name = str(year)
		else:
			month_name = "%s %s" % (datetime.date(year, month, 1).strftime('%B').upper(), str(year))

		for index, row in people.iterrows():

			associates.append({
				'name'   : str(row['Nome']),
				'title'  : str(row['Título']),
				'secret' : row[SECRET_COL_NAME]
			})

			if len(associates) == 4:
				draw_page(pdf, associates, month_name)
				pdf.showPage()

				associates = []
				count += 1

		# Gera a ultima imagem, com 1, 2 ou 3 associados
		if not len(associates) == 0:
			draw_page(pdf, associates, month_name)

		pdf.save()
