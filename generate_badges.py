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

reload(sys)
sys.setdefaultencoding('utf8')
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')



n_args = len(sys.argv)

# Define o nome do arquivo de entrada a partir dos argumentos
if n_args >= 2:
    input_filename = sys.argv[1]
else:
    raise Exception('Qual é o arquivo de entrada?')

# Se o mês for dado como argumento (numérico: 1..12), usa-o;
# se não, usa o mês seguinte ao atual.
if n_args >= 3:
    month = int(sys.argv[2])
else:
    month = datetime.date.today().month + 1

# Se o ano for dado como argumento (numérico), usa-o;
# se não, usa o ano atual.
if n_args >= 4:
    year = int(sys.argv[3])
else:
    year = datetime.date.today().year

# Define os nomes dos dois arquivos de saída: um contendo os crachás (PDF)
# e o outro, os segredos (XLSX).
badges_filename = "./output/%s-%s.pdf" % (year, month)
secrets_filename = "./output/%s-%s_secrets.xlsx" % (year, month)

pdf = canvas.Canvas(badges_filename)
pdf.setFillColor(cfg['COLOR'])
pdf.setFont(cfg['FONT_FAMILY'], cfg['FONT_SIZE'])

SECRET_COL_NAME = 'Segredo'

# Cria um DataFrame com os números de matrícula e nomes dados
# e escolhe aleatoriamente os segredos.
people = read_excel(input_filename, sheetname=0)
seed(int(year + month))
people[SECRET_COL_NAME] = Series(randint(0,100000,size=len(people)))
people.to_excel(secrets_filename, index=False)

# Gera cada uma das imagens, de 4 em 4 associados
associates = []
count = 1
month_name = "%s %s" % (datetime.date(year, month, 1).strftime('%B').upper(), str(year))

for index, row in people.iterrows():

    associates.append({
        'name'   : str(row['Nome']),
        'title'  : str(row['Titulo']),
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
