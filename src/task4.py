#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 03:57:37 2021

@author: Mohamed Gamal
"""



import sys
import datetime
import contextlib
import inspect
import time
import io
import pandas as pd


class decorator_4:
    global dict,res
    res = []
    dict = {}
    
    def __init__(self, fun):
        self.fun = fun
        decorator_4.count = 0

    def __call__(self, *args, **kwargs):
        decorator_4.count += 1
        out = []
        flag = False
        
        def sort(lst):
            lst.sort(key=lambda x: x[1])
            return lst

        def enter_sec(lst,i):
            lst.insert(1,i)
            return lst
        
        with contextlib.redirect_stdout(io.StringIO()) as f:
            try:
                start = time.perf_counter()
                out = self.fun(*args, **kwargs)
                end = time.perf_counter()
                flag = True
            except:
                err = str(sys.exc_info()[1])
                print(err)
                with open('log.txt', 'a') as writer:
                    ct = str(datetime.datetime.now())
                    writer.writelines(self.fun.__name__+":\tcurrent time:-"+ct +"\tThe error is:\t"+err+'\n')
        if flag:
            s = f.getvalue()
            
            if self.fun.__name__ in dict:
                return
            else:
                dict[self.fun.__name__] = end-start
    
            if len(dict) == 4:
                res = [[k,v] for k,v in dict.items()]
                final = sort(res)
                rank = [enter_sec(j,i+1) for i,j in enumerate(final)]
                data_frame = pd.DataFrame(rank,columns=["PROGRAM", "RANK","TIME ELAPSED"])
                print(data_frame)
            
            
            with open('output.txt', 'a') as writer:
                writer.writelines(
                    f"{self.fun.__name__} call {decorator_4.count} executed in "+'{0:.4f}'.format(end-start)+" sec\n")
                writer.writelines(f"Name:\t{self.fun.__name__}\n")
                writer.writelines(f"Type:\t{type(self.fun)}\n")
                writer.writelines(f"Sign:\t{inspect.signature(self.fun)}\n")
                writer.writelines(
                    f"Args:\tpositional {args}\n\tkey=worded{kwargs}\n")
                writer.writelines(f"Doc:\t{self.fun.__doc__}\n")
                temp = '\t'
                writer.writelines(
                    f"Source:{temp.join([line for line in inspect.getsourcelines(self.fun)[0]])}")
                writer.writelines("\n")
                writer.writelines(f"Output:\n{s}")
                writer.writelines("\n")

        return out


