# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lis = []
        temp = head
        last_temp = None
        while temp:
            if temp.val in lis:
                last_temp.next = temp.next
            else:
                lis.append(temp.val)
                last_temp = temp
            temp = temp.next
        return head