#!usr/bin/env python
#-*- coding: utf-8 -*-

def search(n, arr):
    index = None
    for element in arr:
        if element == n:
            index = arr.index(element)
    return index