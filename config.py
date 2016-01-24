from reportlab.lib.colors import Color

cfg = {
  'TITLE_COL_INDEX': 0,
  'NAME_COL_INDEX': 1,
  'PLATE_1_COL_INDEX': 5,
  'PLATE_2_COL_INDEX': 6,
  'SECRET_COL_INDEX': 8,
  #'INPUT_FILENAME': "input/associados.csv",
  'INPUT_FILENAME': "input/test/associados.csv",
  #'OUTPUT_FILENAME': "output/crachas.pdf",
  'OUTPUT_FILENAME': "output/test/crachas.pdf",
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
