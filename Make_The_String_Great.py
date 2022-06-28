def makeGood(s: str) -> str:
        str1 = ''
        if s == '':
            return s
        if s.upper() == s or s.lower() == s :
            return s
        i = 0
        arr = []*len(s)
        for i in range(len(s)):
            arr.append(s[i])
        print (arr)
        for i in range(-1, len(s)-1):
            if s[i] == (s[i+1]).upper() or s[i].upper() == (s[i+1]):
                print (s[i], s[i+1], i , i+1)
            else:
                str1 += s[i]
        return str1
                
                
                
print(makeGood("abBAcC"))