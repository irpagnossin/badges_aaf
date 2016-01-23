#!/usr/bin/env python
# -*- coding: utf-8 -*-
from read_csv import read_csv
from draw_page import draw_page
from reportlab.pdfgen import canvas

CODE_ROW_INDEX = 0#<--- 8
NAME_ROW_INDEX = 1
INPUT_FILENAME = "input/associados.csv"
OUTPUT_FILENAME = "output/crachas.pdf"


pdf = canvas.Canvas(OUTPUT_FILENAME)

# Gera cada uma das imagens, de 4 em 4 associados
names = []
codes = []
count = 1
for row in read_csv(INPUT_FILENAME):

    names.append(row[NAME_ROW_INDEX])
    codes.append(row[CODE_ROW_INDEX])

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
