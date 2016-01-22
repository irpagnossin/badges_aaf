#!/usr/bin/env python
# -*- coding: utf-8 -*-
from read_csv import read_csv
from generate_image import generate_image

CODE_ROW_INDEX = 8
NAME_ROW_INDEX = 1

# Gera cada uma das imagens, de 4 em 4 associados
names = []
codes = []
count = 1
for row in read_csv("input/associados_teste.csv"):

    names.append(row[NAME_ROW_INDEX])
    codes.append(row[CODE_ROW_INDEX])

    if len(names) == 4:
        image_filename = "output/img_" + str(count) + ".jpg"
        generate_image(image_filename, names, codes)

        codes = []
        names = []
        count += 1

# Gera a última imagem, com 1, 2 ou 3 associados
if not len(names) == 0:
    image_filename = "output/img_" + str(count) + ".jpg"
    generate_image(image_filename, names, codes)
