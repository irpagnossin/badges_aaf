#!/usr/bin/env python
# -*- coding: utf-8 -*-
from read_csv import read_csv
from draw_page import draw_page
from reportlab.pdfgen import canvas
from config import cfg

pdf = canvas.Canvas(cfg['OUTPUT_FILENAME'])
pdf.setFont("Helvetica", 12)

# Gera cada uma das imagens, de 4 em 4 associados
associates = []
count = 1
for row in read_csv(cfg['INPUT_FILENAME']):

    plates = [row[cfg['PLATE_1_COL_INDEX']], row[cfg['PLATE_2_COL_INDEX']]] # TODO: tornar independente da quantidade de placas

    associates.append({
        'name': row[cfg['NAME_COL_INDEX']],
        'title': row[cfg['TITLE_COL_INDEX']],
        'secret': row[cfg['SECRET_COL_INDEX']],
        'plates': filter(lambda x: not x == '', plates), # Apenas as placas não nulas
    })

    if len(associates) == 4:
        draw_page(pdf, associates)
        pdf.showPage()

        associates = []
        count += 1

# Gera a última imagem, com 1, 2 ou 3 associados
if not len(associates) == 0:
    draw_page(pdf, associates)

pdf.save()
