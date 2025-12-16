"""
https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

def pig_it(text):
    result = ''
    for word in text.split():
        if not word.isalpha():
            result += word
            result += ' '
        else:
            result += word[1:]
            result += word[0]
            result += 'ay '
    return result[:-1]