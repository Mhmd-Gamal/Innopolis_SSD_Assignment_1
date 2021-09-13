#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 19:25:54 2021

@author: Mohamed Gamal
"""

from task1 import decorator_1
from task2 import decorator_2
from task3 import decorator_3
from task4 import decorator_4
from math import sqrt
import cmath


'''
============================================================================================================

                    Please uncomment proposed decorator to run

============================================================================================================
'''

### Pascal Triangle

#@decorator_1
#@decorator_2
#@decorator_3
@decorator_4
def pascal_triangle(n):
    ''''
    prints the first n rows of pascals triangle
    '''
    trow = [1]
    y = [0]
    for x in range(max(n,0)):
        print(trow)
        trow=[l+r for l,r in zip(trow+y, y+trow)]
 

     
### Quadratic Equation
        
#@decorator_1
#@decorator_2
#@decorator_3
@decorator_4
def quad(a, b, c):
    """
    Quadratic equation solver
    """
    d = (b ** 2) - (4 * a * c)
    f_ans = (-b - cmath.sqrt(d)) / (2 * a)
    s_ans = (-b + cmath.sqrt(d)) / (2 * a)
    return f_ans, s_ans

# Another approach using lambda
def quad_lambda(a,b,c):
    return lambda a, b, c: ((-b + sqrt((b * b) - (4 * a * c))) / (2 * a), (-b - sqrt((b * b) - (4 * a * c))) / (2 * a))



### palindromes
    
#@decorator_1
#@decorator_2
#@decorator_3
@decorator_4
def palindromes(words):
    '''
    Find palindromes in a given list of strings
    '''
    result = list(filter(lambda x: (x == "".join(reversed(x))), words))
    return result


### element-wise function
    
#@decorator_1
#@decorator_2
#@decorator_3
@decorator_4
def elem_wise(list1, list2):
    '''
    This function element-wise sum on two lists 
    after 2 nd power transformation of each element
    '''
    res = [i**2 + j**2 for i, j in zip(list1, list2)]
    return res




if __name__ == '__main__':
    pascal_triangle(5)
    quad(3,4,56)
    palindromes(["php", "Innopolis", "Python", "Pop", "Java", "aaa"])
    elem_wise([1, 2, 3, 4, 5], [6, 7, 8, 9])
    