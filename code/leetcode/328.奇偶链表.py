# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        temp1 = head
        temp2 = head.next
        temp = None
        while temp2 and temp2.next:
            temp = temp2.next.next
            temp2.next.next = temp1.next
            temp1.next = temp2.next
            temp2.next = temp
            temp2 = temp
            temp1 = temp1.next
        return head

            
        