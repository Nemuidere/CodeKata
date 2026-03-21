"""
You might already be familiar with many smartphones that allow you to use a geometric pattern as a security measure. To unlock the device, you need to connect a sequence of dots/points in a grid by swiping your finger without lifting it as you trace the pattern through the screen.

The image below has an example pattern of 7 dots/points: (A -> B -> I -> E -> D -> G -> C).

For this kata, your job is to implement a function that returns the number of possible patterns starting from a given first point, that have a given length.

More specifically, for a function countPatternsFrom(firstPoint, length), the parameter firstPoint is a single-character string corresponding to the point in the grid (e.g.: 'A') where your patterns start, and the parameter length is an integer indicating the number of points (length) every pattern must have.

For example, countPatternsFrom("C", 2), should return the number of patterns starting from 'C' that have 2 two points. The return value in this case would be 5, because there are 5 possible patterns:

(C -> B), (C -> D), (C -> E), (C -> F) and (C -> H).

Bear in mind that this kata requires returning the number of patterns, not the patterns themselves, so you only need to count them. Also, the name of the function might be different depending on the programming language used, but the idea remains the same.

Rules
In a pattern, the dots/points cannot be repeated: they can only be used once, at most.
In a pattern, any two subsequent dots/points can only be connected with direct straight lines in either of these ways:
Horizontally: like (A -> B) in the example pattern image.
Vertically: like (D -> G) in the example pattern image.
Diagonally: like (I -> E), as well as (B -> I), in the example pattern image.
Passing over a point between them that has already been 'used': like (G -> C) passing over E, in the example pattern image. This is the trickiest rule. Normally, you wouldn't be able to connect G to C, because E is between them, however when E has already been used as part the pattern you are tracing, you can connect G to C passing over E, because E is ignored, as it was already used once.

The sample tests have some examples of the number of combinations for some cases to help you check your code.
"""

import string

def count_patterns_from(firstPoint, length):

    if length <= 0: return 0
    if length > 9: return 0
    if length == 1: return 1

    class Dot:
        def __init__(self, name):
            self.name = name
            self.isUsed = False
            self.blockedBy = []
        
        def add_block(self, first, second):
            self.blockedBy.append((first, second))
            
        def check_block(self, value, position):
            return any(pair[position] == value for pair in self.blockedBy)
    
    def calculate_connections(currentDot, length):
        if length == 1:
            return 1

        count = 0
        currentDot.isUsed = True

        for name, dot in dots.items():
            can_move = False
            if not dot.isUsed:
                can_move = True

                for left, right in currentDot.blockedBy:
                    if right == name:
                        if not dots[left].isUsed:
                            can_move = False
                            break
            
            if can_move:
                count += calculate_connections(dot, length-1)


        currentDot.isUsed = False
        return count

    dots = {letter: Dot(letter) for letter in string.ascii_uppercase[:9]}
    
    dots['A'].add_block('B', 'C')
    dots['A'].add_block('E', 'I')
    dots['A'].add_block('D', 'G')
    dots['B'].add_block('E', 'H')
    dots['C'].add_block('B', 'A')
    dots['C'].add_block('E', 'G')
    dots['C'].add_block('F', 'I')
    dots['D'].add_block('E', 'F')
    dots['F'].add_block('E', 'D')
    dots['G'].add_block('D', 'A')
    dots['G'].add_block('E', 'C')
    dots['G'].add_block('H', 'I')
    dots['H'].add_block('E', 'B')
    dots['I'].add_block('H', 'G')
    dots['I'].add_block('E', 'A')
    dots['I'].add_block('F', 'C')

    return calculate_connections(dots[firstPoint], length)