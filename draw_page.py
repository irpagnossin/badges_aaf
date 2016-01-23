#!/usr/bin/env python
# -*- coding: utf-8 -*-
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics import renderPDF
from reportlab.lib.units import cm
from datetime import date
from config import cfg
from reportlab.pdfbase.pdfmetrics import stringWidth

BKG_WIDTH = 2 * cfg['BKG_WIDTH'] * cm
BKG_HEIGHT = 2 * cfg['BKG_HEIGHT'] * cm

def draw_page(canvas, names, codes):

    names = map(str.upper, names)
    canvas.drawImage(cfg['BKG'], 0, 0, width=BKG_WIDTH, height=BKG_HEIGHT)

    for i in range(len(names)):
        name = names[i]
        code = codes[i]
        draw_name(canvas, trip(name), cfg['NAME_SPOTS'][i])
        draw_code(canvas, name, codes[i], cfg['CODE_SPOTS'][i])

def draw_name(canvas, name, (x,y)):
    canvas.setFont("Helvetica", 12)
    canvas.drawCentredString(x, y, name.decode('utf-8', errors='ignore'))

def draw_code(canvas, name, code, (x,y)):
    qrcode_content = 'Associação Atlética Floresta, ' + str(date.today().year) + ' | ' + name + ' | ' + str(code)
    q = QrCodeWidget(qrcode_content)
    q.barHeight = 100
    q.barWidth = 100
    d = Drawing()
    d.add(q)
    renderPDF.draw(d, canvas, x-q.barWidth/2, y-q.barHeight/2)

def trip(name):
    max_length = 28
    return name[0:max_length-3] + "..." if len(name) > max_length else name
