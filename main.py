#!/usr/bin/env python
# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
kivy.require('2.2.1') # replace with your current kivy version !
import datetime
import locale
import os

from generate_badges import generate_badges

import sys
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')


class Root(FloatLayout):

    year = ObjectProperty(None)
    month = ObjectProperty(None)
    input_filename_btn = ObjectProperty(None)
    input_filename = ''

    def default_year(self):
        today = datetime.date.today()
        year = today.year if today.month < 12 else today.year + 1
        return str(year)

    def default_month(self):
        month = datetime.date.today().month + 1
        if month == 13:
            month = 1
        return str(month)

    def gui_generate_badges(self):

        month = int(self.month.text)
        year = int(self.year.text)

        anualistas = month == 0

        if anualistas:
            badges_filename = "./output/%s.pdf" % year
            secrets_filename = "./output/%s_secrets.xlsx" % year
        else:
            badges_filename = "./output/%s-%s.pdf" % (year, month)
            secrets_filename = "./output/%s-%s_secrets.xlsx" % (year, month)

        generate_badges(self.input_filename, badges_filename, secrets_filename, month, year)

        message = 'Os seguintes arquivos foram gerados:\n%s: contém os crachás.\n%s: contém os segredos.' % (badges_filename, secrets_filename)

        popup = Popup(title='Resumo',
                content=Label(text=message),
                size = (200,200),
                auto_dismiss=False)
        popup.open()

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Escolha o arquivo com a lista de associados", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.input_filename = filename[0]
            self.input_filename_btn.text = 'Arquivo de associados: ' + filename[0]
            self.generate_badges_btn.disabled = False

        self.dismiss_popup()

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class MyApp(App):
    title = 'Associação Atlética Floresta :: Gerador de crachás v0.1 (2016)'
    pass

Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)

if __name__ == '__main__':
    MyApp().run()
