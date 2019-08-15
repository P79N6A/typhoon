# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        two_step = head.next
        one_step = head
        if two_step is None:
            return one_step
        while two_step is not None and two_step.next:
            two_step = two_step.next.next
            if two_step is not None:
                one_step = one_step.next
        return one_step.next
        