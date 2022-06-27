def strStr(haystack, needle):
    if needle == '':
        return 0
    else:
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)
        
print(strStr('hello', 'll'))