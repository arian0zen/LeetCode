#unsolved

def isInterleave(s1, s2, s3):
    s1 = list(s1)
    s2 = list(s2)
    s3 = list(s3)
    
    for i in range(len(s3)):
        if len(s1) == 0 or len(s2) == 0:
            break
        print(len(s1))
        if s1[0] == s3[0]:
            s1.pop(0)
            s3.pop(0)
        elif s2[0] == s3[0]:
            s2.pop(0)
            s3.pop(0)
        print (s1, s2)
        print(s3)
    return s3
            
        
    
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(isInterleave(s1, s2, s3))