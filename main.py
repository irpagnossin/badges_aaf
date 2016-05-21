#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import easygui
#path = easygui.fileopenbox()
#print path

msg = "Preencha as informações abaixo"
title = "Associação Atlética Floresta"
fieldNames = ["Ano", "Mês"]
fieldValues = easygui.multenterbox(msg, title, fieldNames)
if fieldValues is None:
    sys.exit(0)
# make sure that none of the fields were left blank
while 1:
    errmsg = ""
    for i, name in enumerate(fieldNames):
        if fieldValues[i].strip() == "":
          errmsg += "{} is a required field.\n\n".format(name)
    if errmsg == "":
        break # no problems found
    fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
    if fieldValues is None:
        break
print("Reply was:{}".format(fieldValues))
