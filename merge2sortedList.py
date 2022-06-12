#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
import sys
sys.setrecursionlimit(1000000)
#Function to merge two sorted linked list.
class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 == None and list2 == None:
            return None
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        head = 0
        if list1.val < list2.val:
            head = list1
            head.next = self.mergeTwoLists(list1.next,list2)
        else: #when list1 >= list2
            head = list2
            head.next = self.mergeTwoLists(list1, list2.next)
            
        return head
        