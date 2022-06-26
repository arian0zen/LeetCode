
def minDistance(word1, word2):
    n , m = len(word1), len(word2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for c in range(n+1):
        dp[0][c] = c
        
    for r in range(m+1):
        dp[r][0] = r
    
    for r in range(1,m+1):
        for c in range(1,n+1):
            if word1[c-1] == word2[r-1]:
                dp[r][c] = dp[r-1][c-1]
            else:
                dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1])
    return dp[-1][-1]
    
       
    
print(minDistance('sea', 'ate'))



''''

#in the above example time O(m*n) space O(m*n) because of the 2d array we created.
we can optimize the space uptop O(m) if we just use 2 array inline instead of matrix, below is the code

 """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1,l2=len(word1)+1,len(word2)+1
        dp=range(l2)
        for i in range(1,l1):
            curr=[i]*l2
            # print(curr)
            for j in range(1,l2):
                if word1[i-1]==word2[j-1]:
                    
                    curr[j]=dp[j-1]
                    print(curr, "when j is:", j, i)
                else:
                    print(curr)
                    print(dp[j-1])
                    curr[j]=min(dp[j-1]+1,dp[j],curr[j-1])+1
                    print(curr)
            dp=curr
        return dp[-1] if l1 and l2 else abs(l1-l2)


'''