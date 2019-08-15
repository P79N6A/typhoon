# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        listNode1 = head
        while listNode1:
            listNode2 = listNode1.next
            if listNode2:
                listNode1.val,listNode2.val = listNode2.val,listNode1.val
                listNode1 = listNode2.next
            else:break
        return head