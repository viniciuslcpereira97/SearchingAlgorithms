#!usr/bin/env python
#-*- coding: utf-8 -*-

from datetime import datetime

import linear_search as linear
import binary_search as binary
import jump_search as jump

n = 255
arr = range(0, 255)

# print linear.search(n, arr)
# print linear.recursive(n, arr)
# print binary.recursive(n, arr)
print jump.search(n, arr)