
from read_csv import read_csv
from draw_page import draw_page
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from config import cfg
from pandas import read_excel, Series
from numpy.random import seed, randint
import datetime
import locale

pdf = canvas.Canvas(cfg['OUTPUT_FILENAME'])
pdf.setFillColor(cfg['COLOR'])
pdf.setFont("Helvetica", 12)

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

# Gera cada uma das imagens, de 4 em 4 associados
associates = []
count = 1

year = int(cfg['YEAR'])
month = int(cfg['MONTH'])

name_column_title = cfg['NAME_COL_NAME']
title_column_title = cfg['TITLE_COL_NAME']
secret_column_title = 'Secret'

people = read_excel(cfg['INPUT_FILENAME'], sheetname=0)
seed(int(year + month))
people[secret_column_title] = Series(randint(0,100000,size=len(people)))

for index, row in people.iterrows():

    associates.append({
        'name': str(row[name_column_title]),
        'title': str(row[title_column_title]),
        'secret': row[secret_column_title]
    })
    
    print associates

    month_year = "%s %s" % (datetime.date(year, month, 1).strftime('%B').upper(), str(year))

    if len(associates) == 4:
        draw_page(pdf, associates, month_year)
        pdf.showPage()

        associates = []
        count += 1

# Gera a ultima imagem, com 1, 2 ou 3 associados
if not len(associates) == 0:
    draw_page(pdf, associates, month_year)

pdf.save()

people.to_excel(cfg['SECRETS_FILE'], index=False)
