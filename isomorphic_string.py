#Python || faster than 99.21% || 30ms LeetCode


def isIsomorphic(s,t):
    
    map_s = {}
    if (len(set(s)) != len(set(t))):
        return False
    
    
    for i in range(len(s)):
        if s[i] not in map_s :
            map_s[(s[i])]= t[i]
        # print (map_s)
        # for i in range(len(s)):
        print( map_s[(s[i])], t[i] )
        if map_s[(s[i])] != t[i]:
            return False
    return True
        
    
    
a = "badc"
b = "baba"
print(isIsomorphic(a,b))

#Python || faster than 99.21% || 30~50ms
