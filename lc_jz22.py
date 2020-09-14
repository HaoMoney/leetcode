# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        cur = ListNode(0)
        cur = head
        length = 0
        if not head:
            return None
        while head.next:
            length += 1
            head = head.next
        for _ in range(length-k+1):
            cur = cur.next
        return cur
