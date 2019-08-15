# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        temp = head
        last_temp = None
        while temp:
            temp_next = temp.next
            temp.next = last_temp
            last_temp = temp
            temp = temp_next
        return last_temp