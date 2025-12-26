"""
https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python

A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
"""

def solution(args):
    result = ''
    last = 999
    dash = False
    count = 1
    for x in args:
        if (x - 1) == last:
            count += 1
            if dash == False:
                if count >= 3:
                    result = result[:-1]
                    result += '-'
                    dash = True
        else:
            if count == 2:
                result += str(last) + ','
            if dash == True: 
                result += str(last) + ','
                dash = False
            result += str(x) + ','
            count = 1
        last = x
    if dash == True: 
        result += str(args[-1])
    if count == 2:
        result += str(last)
    if result[-1] == ',':
        result = result[:-1]
    return result