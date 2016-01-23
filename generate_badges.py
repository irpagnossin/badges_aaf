#!/usr/bin/env python
# -*- coding: utf-8 -*-
from read_csv import read_csv
from draw_page import draw_page
from reportlab.pdfgen import canvas
from config import cfg

pdf = canvas.Canvas(cfg['OUTPUT_FILENAME'])

# Gera cada uma das imagens, de 4 em 4 associados
names = []
codes = []
count = 1
for row in read_csv(cfg['INPUT_FILENAME']):

    names.append(row[cfg['NAME_COL_INDEX']])
    codes.append(row[cfg['CODE_COL_INDEX']])

    if len(names) == 4:
        draw_page(pdf, names, codes)
        pdf.showPage()

        codes = []
        names = []
        count += 1

# Gera a última imagem, com 1, 2 ou 3 associados
if not len(names) == 0:
    draw_page(pdf, names, codes)

pdf.save()
