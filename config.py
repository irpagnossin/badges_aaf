#!/usr/bin/env python
# -*- coding: utf-8 -*-
from reportlab.lib.colors import Color

cfg = {
  'TITLE_COL_NAME': 'Titulo',
  'NAME_COL_NAME': 'Nome',
  'YEAR': 2016,
  'MONTH': 5, # eg., se maio, 5; se janeiro, 1
  'INPUT_FILENAME': "input/maio_2016_compl.xlsx",
  'OUTPUT_FILENAME': "output/maio_2016_compl.pdf",
  'SECRETS_FILE': 'output/maio_2016_compl_secrets.xlsx',
  'BKG': "input/background.png",
  'BKG_WIDTH': 9,
  'BKG_HEIGHT': 13,
  'NAME_SPOTS': [(127,195),(385,195),(127,561),(385,561)],
  'TITLE_SPOTS': [(127,173),(382,173),(127,540),(382,540)],
  'PLATE_SPOTS': [(20,33), (275,33), (20, 400), (275,400)],
  'QR_SPOTS': [(200,57),(454,57),(200,425),(454,425)],
  'DATE_POS': [(127,125),(385,125),(127,501),(385,501)],
  'COLOR': Color(0.38,0.10,0.28)
}
