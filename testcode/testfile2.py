#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports-----------------------------------------------------------------------

#--Python Imports.
import os
import sys

if __name__ == '__main__':
    lst = []
    for i in range(100):
        lst.append(i)
        lst.reverse()
    print(lst)