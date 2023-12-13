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

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

def generate_badges(input_filename, badges_filename, secrets_filename, month, year):


    pdf = canvas.Canvas(badges_filename)
    pdf.setFillColor(cfg['COLOR'])
    pdf.setFont(cfg['FONT_FAMILY'], cfg['FONT_SIZE'])

    SECRET_COL_NAME = 'Segredo'

    # Cria um DataFrame com os números de matrícula e nomes dados
    # e escolhe aleatoriamente os segredos.
    people = read_excel(input_filename)
    seed(int(year + month))
    people[SECRET_COL_NAME] = Series(randint(0,100000,size=len(people)))
    people.to_excel(secrets_filename, index=False)

    # Gera cada uma das imagens, de 4 em 4 associados
    associates = []
    count = 1

    anualistas = month == 0

    if anualistas:
        month_name = str(year)
    else:
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
