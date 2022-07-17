#iterative appoach O(n) O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = None
        while head != None:
            next = head.next
            head.next = temp
            temp = head
            head = next
        return temp

'''

#recursive implementation O(n) O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        newHead = self.reverseList(head.next)
        next_head = head.next
        next_head.next = head
        head.next = None
        return newHead


'''

#but as always, recursive approach generates a little more cache, so more space needed