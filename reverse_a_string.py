import re


def reverseString(s):
    l = len(s)-1
    for i in range(len(s)//2):
        s[i],s[l-i]  = s[l-i],s[i]
    return s

s = ['a', 'r', 'i', 'a', 'n']
print(reverseString(s))