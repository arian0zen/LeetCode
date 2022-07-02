def maxArea(h, w, hCuts, vCuts):
    
    hCuts.sort()
    vCuts.sort()
        
    hCuts = [0] + hCuts +[h]
    vCuts = [0] + vCuts + [w]
        
    cakeSize_hCut=0
    cakeSize_vCut=0
    for i  in range(1, len(hCuts)):
        diff_hCut=(hCuts[i] - hCuts[i-1])
        cakeSize_hCut=max(cakeSize_hCut,diff_hCut)
        
    for j in range(1, len(vCuts)):
        diff_vCut=(vCuts[j] - vCuts[j-1])
        cakeSize_vCut=max(cakeSize_vCut,diff_vCut)
    return (cakeSize_hCut * cakeSize_vCut)% ((10**9)+7)
    
    
    
    
    
    
    
    
    
h = 5
w = 4
horizontalCuts = [1,2,4]
verticalCuts = [1,3]
    
print(maxArea(h, w, horizontalCuts, verticalCuts))