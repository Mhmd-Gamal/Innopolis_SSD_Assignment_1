#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 01:58:47 2021

@author: Mohamed Gamal
"""
import time
import io
import contextlib
import inspect

def decorator_2(fun):
    def wrapper(*args,**kwargs):
        wrapper.count += 1
        with contextlib.redirect_stdout(io.StringIO()) as f:
            start = time.perf_counter()
            fun(*args)
            end = time.perf_counter()
        s = f.getvalue()
        print(f"{fun.__name__} call {wrapper.count} executed in " +
              '{0:.4f}'.format(end-start)+" sec")
        print("Name:    ", fun.__name__)
        print("Type:    ",type(fun))
        print("Sign:    ",inspect.signature(fun))
        print("Args:",end="    " )
        print("Positional: ",locals()['args'])
        print("         key-worded:  ",locals()['kwargs'])
        print("Doc:     ",inspect.getdoc(fun))
        print("Source:      ",inspect.getsource(fun))
        print("Output:  ",fun(*args,**kwargs))
    wrapper.count = 0
    return wrapper
