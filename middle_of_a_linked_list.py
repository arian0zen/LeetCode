#traverse through the whole list first time and count how many nodes are there
#then traverse only till the mid, total / 2, and return 
#O(n) + O(n) ~ O(n) || O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        current = head
        while current!= None:
            total += 1
            current = current.next
        
        mid = (total // 2) + 1
        
        count = 1
        while head!= None:
            # print(head)
            if count == mid:
                return head
            count += 1
            head = head.next
    
'''

#When traversing the list with a pointer slow, make another pointer fast that traverses twice as fast.
#When fast reaches the end of the list, slow must be in the middle.
#o(n) || O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

'''