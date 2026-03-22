
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

def next_bigger(n):
    input = n

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
            part_b = digits[split_point:]
            part_a = digits[:split_point]

            smallestBigger = 10 #I initially put this as '9' and couldn't figure out why my code didn't work
            smallestBiggerId = 0
            for d in range(len(part_a)):
                if (part_a[d] > part_a[-1]) and (part_a[d] < smallestBigger):
                    smallestBigger = part_a[d]
                    smallestBiggerId = d
            
            part_a[-1], part_a[smallestBiggerId] = part_a[smallestBiggerId], part_a[-1]
            part_a = part_a[:-1]
            part_a.sort(reverse=True)
            part_a.append(smallestBigger)
            digits = part_a + part_b
            break

    result = 0
    digits.reverse()
    for d in digits:
        result = (result* 10) + d

    if result == input:
        return -1
    else:
        return result
