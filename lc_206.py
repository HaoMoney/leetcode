# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last = None
        cur = head
        while head != None:
            cur = head.next
            head.next = last
            last = head
            head = cur
        return last
