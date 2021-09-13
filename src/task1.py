#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 19:26:40 2021

@author: Mohamed Gamal
"""


import time
import contextlib
import io


def decorator_1(fun):
    def wrapper(*args):
        wrapper.count += 1
        with contextlib.redirect_stdout(io.StringIO()) as f:
            start = time.perf_counter()
            fun(*args)
            end = time.perf_counter()
        s = f.getvalue()
        print(f"{fun.__name__} call {wrapper.count} executed in " +
              '{0:.4f}'.format(end-start)+" sec")
    wrapper.count = 0
    return wrapper