#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import qrcode

FONT = ImageFont.truetype("font/Quicksand-Bold.otf", 12)
FONT_COLOR = (0,0,0,255)
NAME_SPOTS = [(155,131),(475,131),(155,593),(475,593)]
CODE_SPOTS = [(211,312),(529,312),(211,782),(529,782)]

def generate_image(filename, names, codes):

    names = map(str.upper, names)

    bkg = Image.open("input/background_teste.png")
    graphics = ImageDraw.Draw(bkg)

    for i in range(len(names)):
        name = names[i]
        code = codes[i]
        draw_name(graphics, trip(name), NAME_SPOTS[i])
        draw_code(graphics, name, codes[i], CODE_SPOTS[i])

    bkg.save(filename)
    bkg.close()

def trip(name):
    return name[0:29] + "..." if len(name) > 32 else name

def draw_name(graphics, name, position):
    width, height = graphics.textsize(name, font=FONT)
    x, y = position[0] - width/2, position[1] - height/2
    graphics.text((x,y), name, font=FONT, fill=FONT_COLOR)

def draw_code(graphics, name, code, (x,y)):
    qr = qrcode.QRCode(
       version=1,
       error_correction=qrcode.constants.ERROR_CORRECT_L,
       box_size=2,
       border=4
    )
    qr.add_data('Associação Atlética Floresta, 2016 | ' + name + ' | ' + str(code))
    qr.make(fit=True)
    ccode = qr.make_image()
    d = ccode.height

    x0 = x - d/2
    y0 = y - d/2
    graphics.rectangle([x0,y0,x0+d-1,y0+d-1], fill="black")
    graphics.bitmap((x0,y0), ccode)
