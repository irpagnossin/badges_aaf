#!/usr/bin/env python
# -*- coding: utf-8 -*-
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics import renderPDF
from reportlab.lib.units import cm
from datetime import date
from config import cfg
from abbreviate import abbreviate

BKG_WIDTH = 2 * cfg['BKG_WIDTH'] * cm
BKG_HEIGHT = 2 * cfg['BKG_HEIGHT'] * cm

def draw_page(canvas, associates):

    canvas.drawImage(cfg['BKG'], 0, 0, width=BKG_WIDTH, height=BKG_HEIGHT)

    names = map(str.upper, [a['name'] for a in associates])
    titles = [a['title'] for a in associates]
    plates = [a['plates'] for a in associates]
    secrets = [a['secret'] for a in associates]

    for i in range(len(names)):
        name = names[i]
        title = titles[i]
        secret = secrets[i]
        draw_name(canvas, abbreviate(name, 27), cfg['NAME_SPOTS'][i])
        draw_title(canvas, title, cfg['TITLE_SPOTS'][i])
        draw_plates(canvas, plates[i], cfg['PLATE_SPOTS'][i])
        draw_code(canvas, name, secret, cfg['QR_SPOTS'][i])

def draw_name(canvas, name, (x,y)):
    canvas.setFont("Helvetica", 14)
    canvas.drawCentredString(x, y, name.decode('utf-8', errors='ignore'))

def draw_title(canvas, title, (x,y)):
    canvas.setFont("Helvetica", 14)
    title = ("TÍTULO: " + title).decode('utf-8', errors='ignore')
    canvas.drawCentredString(x, y, title)

def draw_plates(canvas, plates, (x,y)):
    fontsize = 20
    canvas.setFont("Helvetica", fontsize)
    for i in range(len(plates)):
        canvas.drawString(x, y+fontsize*i, plates[i])

def draw_code(canvas, name, code, (x,y)):
    qrcode_content = 'Associação Atlética Floresta, ' + str(date.today().year) + ' | ' + name + ' | ' + str(code)
    q = QrCodeWidget(qrcode_content)
    q.barHeight = 100
    q.barWidth = 100
    d = Drawing()
    d.add(q)
    renderPDF.draw(d, canvas, x-q.barWidth/2, y-q.barHeight/2)
