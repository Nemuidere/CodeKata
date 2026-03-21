#TODO

"""
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

  12 ==> 21
 513 ==> 531
2017 ==> 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

  9 ==> -1
111 ==> -1
531 ==> -1
"""
int 123 ehehe TO_BE_FINISHED;

def next_bigger(n):

    if n < 10: return -1

    digits = []

    while n > 0:
        digits.append(n % 10) 
        n = n // 10 
    
    for i in range(len(digits) - 1):
        current = digits[i]
        next = digits[i+1]
        
        if current > next:
            split_point = i + 2 
#Error is here, logic should be: 
    #Find the split point
    #Put the NEXT biggest number as the split point
    #Sort the rest of the numbers, ascending
    #TODO
            part_b = digits[split_point:]
            part_a = digits[:split_point]
            part_a.sort()
            digits = part_a + part_b
            break

    result = 0
    digits.reverse()
    for d in digits:
        result = (result* 10) + d

    return result
