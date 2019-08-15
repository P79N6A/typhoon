# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        str1 = ""
        str2 = ""
        temp = l1
        while temp:
            str1 += str(temp.val)
            temp = temp.next
        temp = l2
        while temp:
            str2 += str(temp.val)
            temp = temp.next
        data = int(str1) + int(str2)
        lis = ListNode(0)
        temp = lis
        data_str = str(data)
        for i in range(len(data_str)):
            a = ListNode(int(data_str[i]))
            temp.next = a
            temp = temp.next
        return lis.next
            
            