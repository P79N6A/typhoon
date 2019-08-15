# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        elif head.next is None:
            return True

        two_step = head.next
        one_step = head
        last_one = None

        while two_step is not None and two_step.next:
            two_step = two_step.next.next
            
            two = one_step.next
            one_step.next = last_one
            last_one = one_step
            one_step = two
        
        two = one_step.next
        one_step.next = last_one
            
        if two_step is None:
            one = one_step.next
        else:
            one = one_step
        while one is not None and two is not None:
            if one.val != two.val:
                return False
            one = one.next
            two = two.next
        return True