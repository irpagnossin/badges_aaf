#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

def read_csv(filename):
    with open(filename, "r") as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            yield row
