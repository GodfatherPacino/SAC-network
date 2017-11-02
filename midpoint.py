# !/usr/bin/python27
# coding: utf8

import os,sys,string
from numpy import *


def midp(lst):
    a = array([0, 0, 0])
    a = a.astype('float64')
    for lst1 in lst:
        c = array(lst1).astype('float64')
        a = a + c
    b = a/len(lst)          # b = [1, 2, 3]
    for i in range(len(b)):
        b[i] = round(b[i], 3)
    return b





