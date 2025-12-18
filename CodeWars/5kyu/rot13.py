"""
https://www.codewars.com/kata/530e15517bc88ac656000716/python

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""
def rot13(message):
    result = ''
    for letter in message:
        if letter.isalpha():
            numChar = ord(letter) + 13
            if letter.isupper():
                if numChar > ord('Z'):
                    numChar -= 26
            elif letter.islower():
                if numChar > ord('z'):
                    numChar -= 26
            result += chr(numChar)
        else:
            result += letter
    return result