"""
https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b

The purpose of this kata is to write a program that can do some algebra.

Write a function expand that takes in an expression with a single, one character variable, and expands it. The expression is in the form (ax+b)^n where a and b are integers which may be positive or negative, x is any single character variable, and n is a natural number. If a = 1, no coefficient will be placed in front of the variable. If a = -1, a "-" will be placed in front of the variable.

The expanded form should be returned as a string in the form ax^b+cx^d+ex^f... where a, c, and e are the coefficients of the term, x is the original one character variable that was passed in the original expression and b, d, and f, are the powers that x is being raised to in each term and are in decreasing order.

If the coefficient of a term is zero, the term should not be included. If the coefficient of a term is one, the coefficient should not be included. If the coefficient of a term is -1, only the "-" should be included. If the power of the term is 0, only the coefficient should be included. If the power of the term is 1, the caret and power should be excluded.

Examples:
expand("(x+1)^2")      # returns "x^2+2x+1"
expand("(p-1)^3")      # returns "p^3-3p^2+3p-1"
expand("(2f+4)^6")     # returns "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"
expand("(-2a-4)^0")    # returns "1"
expand("(-12t+43)^2")  # returns "144t^2-1032t+1849"
expand("(r+0)^203")    # returns "r^203"
expand("(-x-1)^2")     # returns "x^2+2x+1"
"""

import math
def expand(expr):

    #Handling input

    expr, n = expr.split("^")
    n = int(n)
    
    expr = expr[1:-1]

    for i, c in enumerate(expr):
        if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
            x = c
            pos = i
            break

    a = expr[:pos]
    if a == "": a = 1
    elif a == "+": a = 1
    elif a == "-": a = -1
    else: a = int(a)

    b = expr.split(x)[1]
    b = int(b)


    if n == 0: return "1"
    if n == 1: return expr


    resList = []

    for k in range(n + 1):

        #Handling math

        res = math.comb(n, k) * (a**(n-k)) * (b**k)
        pwr = n-k

        isPositive = False
        if res > 0: isPositive = True

        isFirst = True
        if k > 0: isFirst = False

        isLast = False
        if k == n + 1: isLast = True

        #Handling the result

        if (res == 1) and (pwr > 0): res = ""
        elif res == -1 and not isLast: res = "-"

        if isPositive and not isFirst:
            if pwr == 1: term = f"+{res}{x}"
            elif pwr == 0: term = f"+{res}"
            else: term = f"+{res}{x}^{pwr}"
        else:
            if pwr == 1: term = f"{res}{x}"
            elif pwr == 0: term = f"{res}"
            else: term = f"{res}{x}^{pwr}"

        resList.append(term)

    final = "".join(resList)
    return final