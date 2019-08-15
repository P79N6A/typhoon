# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp = head
        head = ListNode(0)
        head.next = temp
        last_temp = head
        while temp:
            if temp.val == val:
                last_temp.next = temp.next
            else:
                last_temp = temp
            temp = temp.next
        return head.next

        