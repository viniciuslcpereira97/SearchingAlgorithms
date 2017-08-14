#!usr/bin/env python
#-*- coding: utf-8 -*-

def search(n, arr):
    size = len(arr)
    initial, mid = 0, (size / 2)
    comparator = arr[mid]

    while n != comparator:
        if len(arr) == 1 and arr[0] != n:
            return 
        arr = arr[0:mid] if n < comparator else arr[mid:size]
        size = len(arr)
        mid = (size / 2)
        comparator = arr[mid]
    
    return comparator

def recursive(n, arr):
    size = len(arr)
    mid = (size / 2)
 
    if arr[mid] != n and len(arr) == 1:
        return
    if arr[mid] == n:
        return n
    else:
        if n < arr[mid]:
            return recursive(n, arr[0:mid])
        else:
            return recursive(n, arr[mid:size])