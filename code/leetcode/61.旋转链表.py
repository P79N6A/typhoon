# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        tile = ListNode(0)
        tile.next = head
        temp2 = head
        if temp2 is None:
            return temp2
        len_num = 0
        temp = head
        while temp:
            len_num += 1
            temp = temp.next
        for i in range(k%len_num):
            if temp2.next == None:
                temp2 = head
            else:
                temp2 = temp2.next
        temp1 = tile.next
        while temp2.next:
            temp2 = temp2.next
            temp1 = temp1.next
        temp2.next = head
        tile.next = temp1.next
        temp1.next = None
        return tile.next
            
            
        