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
kivy.require('1.0.6') # replace with your current kivy version !
import datetime
import locale
import os

from generate_badges import generate_badges

import sys
reload(sys)
sys.setdefaultencoding('utf8')
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')


class Root(GridLayout):

    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)


        self.cols = 2

        today = datetime.date.today()

        #
        self.add_widget(Label(text='Ano'))
        self.year = TextInput(multiline=False)
        self.add_widget(self.year)
        self.year.text = str(today.year)

        self.add_widget(Label(text='Mês'))
        self.month = TextInput(multiline=False)
        self.add_widget(self.month)
        self.month.text = str(today.month + 1)

        self.add_widget(Label(text='Arquivo de entrada'))
        self.input_filename = TextInput(multiline=False)
        self.add_widget(self.input_filename)
        #self.input_filename.text = u'./input/maio_2016_compl.xlsx'

        self.generate_badges_btn = Button(text='Gerar crachás e segredos', font_size=14)
        self.add_widget(self.generate_badges_btn)
        self.generate_badges_btn.bind(on_press=self.gui_generate_badges)

        self.choose_file_btn = Button(text='...', font_size=14)
        self.add_widget(self.choose_file_btn)
        self.choose_file_btn.bind(on_press=self.show_load)



    def gui_generate_badges(self, event):

        month = int(self.month.text)
        year = int(self.year.text)

        anualistas = month == 0

        if anualistas:
            badges_filename = "./%s.pdf" % year
            secrets_filename = "./%s_secrets.xlsx" % year
        else:
            badges_filename = "./%s-%s.pdf" % (year, month)
            secrets_filename = "./%s-%s_secrets.xlsx" % (year, month)

        generate_badges(self.input_filename.text, badges_filename, secrets_filename, month, year)

        message = 'Os seguintes arquivos foram gerados:\n%s: contém os crachás.\n%s: contém os segredos.' % (badges_filename, secrets_filename)

        popup = Popup(title='Resumo',
                content=Label(text=message),
                size = (200,200),
                auto_dismiss=False)
        popup.open()

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self, event):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Escolha o arquivo de entrada", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.input_filename.text = filename[0]#stream.read()

        self.dismiss_popup()

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class MyApp(App):

    def build(self):
        return Root()

class BadgeGenerator(App):
    pass

Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)

if __name__ == '__main__':
    MyApp().run()
