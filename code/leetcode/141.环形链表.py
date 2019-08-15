# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        temp_slow = head
        temp_fast = head.next
        while temp_fast is not None and temp_fast.next is not None:
            if temp_slow == temp_fast:
                return True
            temp_slow = temp_slow.next
            temp_fast = temp_fast.next.next
        return False