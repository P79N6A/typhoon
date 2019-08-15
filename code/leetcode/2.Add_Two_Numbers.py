# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
		data1 = ""
        data2 = ""
        while l1:
            data1 = str(l1.val) + data1
            l1 = l1.next
        while l2:
            data2 = str(l2.val) + data2
            l2 = l2.next
        data3 = str(int(data1) + int(data2))
        l3 = None
        l4 = None
        for ch in data3:
            if l3:l4 = l3
            l3 = ListNode(int(ch))
            if l4:l3.next = l4
        return l3