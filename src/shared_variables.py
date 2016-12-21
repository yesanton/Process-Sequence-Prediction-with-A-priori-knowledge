'''
This file was created in order to bring
common variables and functions into one file to make
code more clear

Author: Anton Yeshchenko
'''

ascii_offset = 161

def getUnicode_fromInt(ch):
    return unichr(int(ch) + ascii_offset)

def getInt_fromUnicode(unch):
    return (int(ord(unch)) - ascii_offset)
