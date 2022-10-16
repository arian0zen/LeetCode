def convertToBST(nums):
    def helper(l, r, array):
        if l > r:
            return None
        mid = (l + r) // 2
        array.append(nums[mid])
        helper(l, mid-1, array)
        helper(mid+1, r, array)
        return array
    return helper(0, len(nums) - 1, [])


nums = [-10,-3,0,5,9]
print(convertToBST(nums))

#return the traversal of the BST
