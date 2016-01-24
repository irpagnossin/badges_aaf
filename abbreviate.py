#!/usr/bin/env python
# -*- coding: utf-8 -*-
def abbreviate(name, limit = 20):

    if limit < 4:
        raise ValueError("limit must be >= 3")

    abbreviated_name = name

    if len(abbreviated_name) <= limit:
        return abbreviated_name

    names = abbreviated_name.split(" ")
    if len(names) > 1:
        for i in range(1,len(names)-1):
            if len(names[i]) > 1:
                names[i] = names[i][:1] + "."
            abbreviated_name = " ".join(names)
            if len(abbreviated_name) <= limit:
                break

    if len(abbreviated_name) > limit:
        abbreviated_name = abbreviated_name[0:limit-3] + "..."

    return abbreviated_name
