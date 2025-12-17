"""
https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python

In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

Create as many "shufflings" as you can!

Examples:

With input 'a':
Your function should return: ['a']

With input 'ab':
Your function should return ['ab', 'ba']

With input 'abc':
Your function should return ['abc','acb','bac','bca','cab','cba']

With input 'aabb':
Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
Note: The order of the permutations doesn't matter.

Good luck!
"""


def permutations(s):
    results = [[]]
    for letter in s:
        new_result = []
        for perm in results:
            for i in range(len(perm) + 1):
                temp = perm[:]
                temp.insert(i, letter)
                new_result.append(temp)
        results = new_result
    final = ["".join(p) for p in results]
    final = set(final)
    return final