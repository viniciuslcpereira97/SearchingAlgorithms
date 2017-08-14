#!usr/bin/env python
#-*- coding: utf-8 -*-

from math import sqrt

def search(n, arr):
    size = len(arr)
    jump_block = int(sqrt(size))
    start, end = 0, jump_block
    
    while arr[end] < n:
        start = (end + 1)
        if size - (end + jump_block) < jump_block:
            end = (end + jump_block) + (size - (end + jump_block))
            break
        else:
            end = end + jump_block

    for x in arr[start:end]:
        if x == n:
            return n