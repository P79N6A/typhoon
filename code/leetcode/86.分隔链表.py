# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        tile = ListNode(0)
        tile.next = head
        temp = tile
        temp2 = tile
        while temp2.next:
            if temp2.next.val < x:
                if temp != temp2: 
                    next_temp2 = temp2.next
                    temp2.next = temp2.next.next
                    next_temp2.next = temp.next
                    temp.next = next_temp2
                    temp = temp.next
                else:
                    temp2 = temp2.next
                    temp = temp.next
            else:
                temp2 = temp2.next
        return tile.next