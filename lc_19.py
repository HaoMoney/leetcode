# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None or head.next==None:
            return None
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        if fast == None:      #删除倒数第(链表长度)节点时候需单独判断
            return head.next 

        while fast.next != None:

            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
