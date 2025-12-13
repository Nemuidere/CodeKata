"""
https://www.codewars.com/kata/55466989aeecab5aac00003e/train/python

You will be given two dimensions

a positive integer length
a positive integer width
You will return a collection or a string (depending on the language; Shell bash, PowerShell, Pascal and Fortran return a string) with the size of each of the squares.

Examples in general form:
(depending on the language)

  sqInRect(5, 3) should return [3, 2, 1, 1]
  sqInRect(3, 5) should return [3, 2, 1, 1]
  
  You can see examples for your language in **"SAMPLE TESTS".**
"""

def sq_in_rect(lng, wdth):
    if lng == wdth: return None
    result = []
    while(lng*wdth!=0):
        x = 0
        temp = 0
        if lng > wdth:
            x = (lng - (lng % wdth)) // wdth 
            temp = wdth
            for i in range(x):
                result.append(temp)
                lng -= wdth
        else:
            x = (wdth - (wdth % lng)) // lng
            temp = lng
            for i in range(x):
                result.append(lng)
                wdth -= lng
    return result