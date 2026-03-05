#TODO 

"""
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:


NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

"""
int 123 ehehe TO_BE_FINISHED;

def snail(arr):
    n_right = len(arr)
    n_bottom = len(arr[0]) - 1
    n_left = 1
    n_top = 0

    result = []
    for num in arr[0]:
        result.append(num)

    while(True):
        for i in range(n_left, n_right):
            result.append(arr[i][n_bottom])
        if n_bottom == 0: break;
        n_bottom = n_bottom - 1
        print(result)

        for i in range(n_top, n_bottom + 1):
            result.append(arr[n_right-1][n_bottom-i])
        if n_right == 0: break;
        n_right = n_right - 1
        print(result)

        for i in range(n_left, n_right):
            result.append(arr[n_right - i][n_bottom - 1])
        if n_bottom == n_top: break;
        n_top = n_top + 1
        print(result)

        for i in range(n_top, n_bottom + 1):
            result.append(arr[n_right - 1][i])
        if n_right == n_left: break;   
        n_left = n_left + 1
        print(result)    

    return(result)