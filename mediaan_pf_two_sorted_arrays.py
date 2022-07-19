def findMedianSortedArrays(nums1, nums2):
    nums1 =  nums1+ nums2
    nums1.sort()
    n = len(nums1)

    if n % 2 != 0:
        mid = nums1[n//2]
        return mid
    elif n%2 ==0:
        mid = n//2
        avg = (nums1[mid] + (nums1[mid-1])) /2
    return avg
nums1 = [1, 2, 3, 6, 9]
nums2 = [2,4,9]
print(findMedianSortedArrays(nums1, nums2))

#not optimal