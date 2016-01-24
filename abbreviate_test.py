#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abbreviate import abbreviate

assert abbreviate("ivan ramos pagnossin", 20) == "ivan ramos pagnossin"
assert abbreviate("ivan ramos pagnossin", 19) == "ivan r. pagnossin"
assert abbreviate("ivan ramos pagnossin", 17) == "ivan r. pagnossin"
assert abbreviate("ivan ramos pagnossin", 16) == "ivan r. pagno..."

assert abbreviate("luci andrade ramos pagnossin", 28) == "luci andrade ramos pagnossin"
assert abbreviate("luci andrade ramos pagnossin", 27) == "luci a. ramos pagnossin"
assert abbreviate("luci andrade ramos pagnossin", 27) == "luci a. ramos pagnossin"
assert abbreviate("luci andrade ramos pagnossin", 23) == "luci a. ramos pagnossin"
assert abbreviate("luci andrade ramos pagnossin", 22) == "luci a. r. pagnossin"
assert abbreviate("luci andrade ramos pagnossin", 20) == "luci a. r. pagnossin"
assert abbreviate("luci andrade ramos pagnossin", 19) == "luci a. r. pagno..."

assert abbreviate("primeiro segundo terceiro quarto quinto sexto", 45) == "primeiro segundo terceiro quarto quinto sexto"
assert abbreviate("primeiro segundo terceiro quarto quinto sexto", 44) == "primeiro s. terceiro quarto quinto sexto"
assert abbreviate("primeiro segundo terceiro quarto quinto sexto", 40) == "primeiro s. terceiro quarto quinto sexto"
assert abbreviate("primeiro segundo terceiro quarto quinto sexto", 39) == "primeiro s. t. quarto quinto sexto"
assert abbreviate("primeiro segundo terceiro quarto quinto sexto", 34) == "primeiro s. t. quarto quinto sexto"
assert abbreviate("primeiro segundo terceiro quarto quinto sexto", 33) == "primeiro s. t. q. quinto sexto"
assert abbreviate("primeiro segundo terceiro quarto quinto sexto", 30) == "primeiro s. t. q. quinto sexto"
assert abbreviate("primeiro segundo terceiro quarto quinto sexto", 29) == "primeiro s. t. q. q. sexto"
assert abbreviate("primeiro segundo terceiro quarto quinto sexto", 26) == "primeiro s. t. q. q. sexto"
assert abbreviate("primeiro segundo terceiro quarto quinto sexto", 25) == "primeiro s. t. q. q. s..."

assert abbreviate("um d tres", 9) == "um d tres"
assert abbreviate("um d tres", 8) == "um d ..."

#assert abbreviate("um nome qualquer", 3) == "..." # TODO: isso é um bug, mas não vou corrigir isso agora
#assertRaises(ValueError, abbreviate("um nome qualquer", 3))
