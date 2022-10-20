# -*- coding: utf-8 -*-
"""
author: Alejandra Jiménez Soto
date: 10/20/2022

"""

def esPalindromo(cad):
    if (cad==cad[::-1]):
        return True
    else:
        return False


def esPalindromoRecur(cad):
    if (len(cad)==1) or (len(cad)==0):
        return True
    else:
        if (cad[0]==cad[-1] and esPalindromoRecur(cad[1:-1])):
            return True
        else:
            return False
print(esPalindromoRecur("reconocer"))
print(esPalindromo("arenera"))