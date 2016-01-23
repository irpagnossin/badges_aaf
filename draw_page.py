#!/usr/bin/env python
# -*- coding: utf-8 -*-
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics import renderPDF
from reportlab.lib.units import cm
from datetime import date

BKG = "input/background_teste.png"
BKG_WIDTH = 2 * 9 * cm
BKG_HEIGHT = 2 * 13 * cm
NAME_SPOTS = [(155,131),(475,131),(155,593),(475,593)]
CODE_SPOTS = [(105,150),(260,155),(105,390),(260,390)]

def draw_page(canvas, names, codes):

    names = map(str.upper, names)
    canvas.drawImage(BKG, 0, 0, width=BKG_WIDTH, height=BKG_HEIGHT)

    for i in range(len(names)):
        name = names[i]
        code = codes[i]
        draw_name(canvas, trip(name), NAME_SPOTS[i])
        draw_code(canvas, name, codes[i], CODE_SPOTS[i])

def draw_name(canvas, name, (x,y)):
    #canvas.setFont("Quicksand-Bold", 14)
    canvas.drawString(x, y, name.decode('utf-8', errors='ignore'))

def draw_code(canvas, name, code, (x,y)):
    qrcode_content = 'Associação Atlética Floresta, ' + str(date.today().year) + ' | ' + name + ' | ' + str(code)
    q = QrCodeWidget(qrcode_content)
    q.barHeight = 100
    q.barWidth = 100
    d = Drawing()
    d.add(q)
    renderPDF.draw(d, canvas, x-q.barWidth/2, y-q.barHeight/2)

def trip(name):
    return name[0:29] + "..." if len(name) > 32 else name
